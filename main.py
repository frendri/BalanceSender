from ui.main_ui import Ui_MainWindow
from ui.confirm_dialog_ui import Ui_Dialog

import sys
import math
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

from utils import *
import string
from json import JSONDecodeError


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setWindowTitle("BalanceSender by tern.trade")

        # get user settings
        self.user_data = get_user_data()
        # fill user settings
        self.ui.paymentPassword.setText(self.user_data.get("pay_pass"))
        self.ui.toApiKey.setText(self.user_data.get("tm_api_key"))
        self.ui.steamId.setText(self.user_data.get("steam_id"))
        # update user settings
        self.ui.toApiKey.textEdited.connect(self.update_tm_key)
        self.ui.paymentPassword.textEdited.connect(self.update_pay_pass)
        self.ui.steamId.textEdited.connect(self.update_steam_id)

        # style counts
        self.ui.rubbleSum.textEdited.connect(self.change_cop_count)
        self.ui.copSum.textEdited.connect(self.change_rub_count)
        self.ui.clearRubSum.textEdited.connect(self.changed_clear_sum)
        self.ui.dollarSum.textEdited.connect(self.change_cent_count)
        self.ui.centSum.textEdited.connect(self.change_dol_count)
        self.ui.clearDolSum.textEdited.connect(self.changed_clear_dol)
        # connect signal
        self.ui.sendButton.clicked.connect(self.send_balance)
        self.ui.sendButton_2.clicked.connect(self.send_wax_balance)

    def changed_clear_dol(self, clear_dol: str):
        try:
            if not clear_dol:
                self.ui.centSum.clear()
                self.ui.dollarSum.clear()
                return
            dol_count = "".join(clear_dol.split())
            if ',' in dol_count:
                dol_count = dol_count.replace(',', '.')
            self.ui.clearDolSum.setText(dol_count)
            dirt_dol = math.floor(float(dol_count)*100/98*1000)/1000
            self.ui.dollarSum.setText(str(dirt_dol))
            self.ui.centSum.setText(str(int(dirt_dol * 1000)))
        except:
            self.show_message_box("Вы ввели недопустимые символы в поле")
            self.ui.dollarSum.clear()
            self.ui.centSum.clear()
            self.ui.clearDolSum.clear()

    def change_cent_count(self, dol_count: str):
        try:
            if not dol_count:
                self.ui.centSum.clear()
                self.ui.clearDolSum.clear()
                return
            dol_count = "".join(dol_count.split())
            if ',' in dol_count:
                dol_count = dol_count.replace(',', '.')
            self.ui.dollarSum.setText(dol_count)
            self.ui.clearDolSum.setText(str(round(float(dol_count)*0.98, 2)))
            self.ui.centSum.setText(str(int(float(dol_count)*1000)))
        except:
            self.show_message_box("Вы ввели недопустимые символы в поле")
            self.ui.dollarSum.clear()
            self.ui.centSum.clear()
            self.ui.clearDolSum.clear()

    def change_dol_count(self, cent_count: str):
        try:
            if not cent_count:
                self.ui.dollarSum.setText('')
                self.ui.clearDolSum.clear()
                return
            cent_count = "".join(cent_count.split())
            new_cent = ""
            for char in cent_count:
                if char in string.digits:
                    new_cent += char
            self.ui.centSum.setText(new_cent)
            self.ui.dollarSum.setText(str(round(float(new_cent)/1000, 3)))
            self.ui.clearDolSum.setText(str(round(float(cent_count)/1000*0.98, 3)))
        except:
            self.show_message_box("Вы ввели недопустимые символы в поле")
            self.ui.centSum.clear()
            self.ui.dollarSum.clear()
            self.ui.clearDolSum.clear()

    def changed_clear_sum(self, clear_rub: str):
        try:
            if not clear_rub:
                self.ui.copSum.clear()
                self.ui.rubbleSum.clear()
                return
            rubble_count = "".join(clear_rub.split())
            if ',' in rubble_count:
                rubble_count = rubble_count.replace(',', '.')
            self.ui.clearRubSum.setText(rubble_count)
            dirt_ruble = math.ceil(float(rubble_count)*100/95*100)/100
            self.ui.rubbleSum.setText(str(dirt_ruble))
            self.ui.copSum.setText(str(int(dirt_ruble*100)))
        except:
            self.show_message_box("Вы ввели недопустимые символы в поле")
            self.ui.clearRubSum.clear()
            self.ui.copSum.clear()
            self.ui.rubbleSum.clear()

    def change_cop_count(self, rubble_count: str):
        try:
            if not rubble_count:
                self.ui.copSum.clear()
                self.ui.clearRubSum.clear()
                return
            rubble_count = "".join(rubble_count.split())
            if ',' in rubble_count:
                rubble_count = rubble_count.replace(',', '.')
            self.ui.rubbleSum.setText(rubble_count)
            self.ui.copSum.setText(str(int(float(rubble_count)*100)))
            self.ui.clearRubSum.setText(str(round(float(rubble_count)*0.95, 2)))
        except:
            self.show_message_box("Вы ввели недопустимые символы в поле")
            self.ui.clearRubSum.clear()
            self.ui.copSum.clear()
            self.ui.rubbleSum.clear()

    def change_rub_count(self, cop_count: str):
        try:
            if not cop_count:
                self.ui.rubbleSum.clear()
                self.ui.clearRubSum.clear()
                return
            cop_count = "".join(cop_count.split())
            new_cop = ""
            for char in cop_count:
                if char in string.digits:
                    new_cop += char
            self.ui.copSum.setText(new_cop)
            self.ui.rubbleSum.setText(str(round(float(new_cop)/100, 2)))
            self.ui.clearRubSum.setText(str(round(float(new_cop)/100*0.95, 2)))
        except:
            self.show_message_box("Вы ввели недопустимые символы в поле")
            self.ui.clearRubSum.clear()
            self.ui.copSum.clear()
            self.ui.rubbleSum.clear()

    def send_wax_balance(self):
        from_key = self.ui.fromWaxKey.text()
        steam_id = self.ui.steamId.text()
        try:
            amount = int(self.ui.centSum.text())
        except ValueError:
            amount = self._get_wax_balance(from_key)

        validate_state, message = self.validate_wax(from_key, steam_id, amount)
        if not validate_state:
            self.show_message_box(message)
            return

        dialog = self.create_dialog_window(from_key, steam_id, amount)
        dialog.ui.label_4.setText("В SteamID")
        dialog.ui.to_key.setText(steam_id)
        dialog.ui.sum.setText(f"{round(amount/1000, 3)}$")
        dialog.accepted.connect(lambda: self.send_wax_request(from_key, steam_id, amount))
        dialog.exec_()

    def send_wax_request(self, from_key: str, steam_id: str, amount: int):
        try:
            r = send_wax_balance(from_key, steam_id, amount)
            json_message = r.json()
            if json_message['success']:
                self.show_message_box("Успешно перенес баланс", "Перенос баланса", QMessageBox.Information)
                self.ui.fromWaxKey.clear()
                self.ui.dollarSum.clear()
                self.ui.centSum.clear()
            else:
                msg = json_message.get('msg')
                if msg == "wrong api":
                    error_message = "Указан неверный API-ключ"
                elif msg == 'Insuficient funds':
                    error_message = "Не хватает баланса"
                else:
                    error_message = r.text
                self.show_message_box("Не получилось перенести баланс:\n" + error_message,
                                      "Перенос баланса", QMessageBox.Warning)
        except Exception as ex:
            error_message = getattr(ex, 'message', repr(ex))
            self.show_message_box("Ошибка во время переноса:\n" + error_message,
                                  "Перенос баланса", QMessageBox.Critical)

    def send_balance(self):
        from_key = self.ui.fromApiKey.text()
        to_key = self.ui.toApiKey.text()
        try:
            amount = int(self.ui.copSum.text())
        except ValueError:
            amount = self._get_tm_balance(from_key)
        pay_pass = self.ui.paymentPassword.text()

        validate_state, message = self.validate(from_key, to_key, amount, pay_pass)
        if not validate_state:
            self.show_message_box(message)
            return

        dialog = self.create_dialog_window(from_key, to_key, amount)
        dialog.accepted.connect(lambda: self.send_request(from_key, to_key, amount, pay_pass))
        dialog.exec_()

    def send_request(self, from_key, to_key, amount, pay_pass):
        try:
            r = send_balance(from_key, to_key, amount, pay_pass)
            json_message = r.json()
            if json_message['success']:
                self.show_message_box("Успешно перенес баланс", "Перенос баланса", QMessageBox.Information)
                self.ui.fromApiKey.clear()
                self.ui.rubbleSum.clear()
                self.ui.copSum.clear()
            else:
                if json_message.get('error') == 'need_payment_password':
                    error_message = "Нужно установить Платежный пароль на аккаунте"
                elif json_message.get('error') == "Bad KEY":
                    error_message = "Указан неверный API-ключ"
                elif "You can send only" in json_message.get('error'):
                    error_message = "Указана неправильная сумма. Возможно у вас не хватает средств"
                else:
                    error_message = r.text
                self.show_message_box("Не получилось перенести баланс:\n" + error_message,
                                      "Перенос баланса")
        except Exception as ex:
            error_message = getattr(ex, 'message', repr(ex))
            self.show_message_box("Ошибка во время переноса:\n" + error_message,
                                  "Перенос баланса", QMessageBox.Critical)

    def create_dialog_window(self, from_key: str, to_key: str, amount: int):
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)

        dialog.setWindowTitle("Подтвердите введеные вами данные")

        dialog.ui.from_key.setText(self._hide_key(from_key))
        dialog.ui.to_key.setText(self._hide_key(to_key))
        dialog.ui.sum.setText(str(round(amount/100, 2)))

        return dialog

    def update_tm_key(self, tm_key: str):
        self.user_data['tm_api_key'] = tm_key
        save_user_data(self.user_data)

    def update_steam_id(self, steam_id: str):
        for char in steam_id:
            if char not in string.digits:
                self.show_message_box("Вы ввели неверный SteamID.\nОн должен состоять только из цифр")
                self.ui.steamId.clear()
                return
        self.user_data['steam_id'] = steam_id
        save_user_data(self.user_data)

    def update_pay_pass(self, pay_pass: str):
        self.user_data['pay_pass'] = pay_pass
        save_user_data(self.user_data)

    def _get_tm_balance(self, api_key: str):
        try:
            response = get_tm_balance(api_key)
            money = int(response.json().get('money')*100)
            return money
        except Exception as ex:
            error_message = getattr(ex, 'message', repr(ex))
            self.show_message_box("Ошибка получения баланса:\n" + error_message,
                                  "Получение баланса", QMessageBox.Critical)

    def _get_wax_balance(self, api_key: str):
        try:
            response = get_wax_balance(api_key)
            money = response.json()['user']['wallet']
            return money
        except Exception as ex:
            error_message = getattr(ex, 'message', repr(ex))
            self.show_message_box("Ошибка получения баланса:\n" + error_message,
                                  "Получение баланса", QMessageBox.Critical)

    @staticmethod
    def show_message_box(message: str, title="Ошибка валидации", level=QMessageBox.Warning):
        msg_box = QMessageBox()
        msg_box.setIcon(level)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.exec_()

    @staticmethod
    def validate(from_key: str, to_key: str, amount: int, pay_pass: str):
        if from_key == '' or to_key == '':
            return False, "Вы не установили API-ключ"
        elif from_key == to_key:
            return False, "Вы установили одинаковые API-ключи"
        elif pay_pass == '':
            return False, "Вы не указали платежный пароль"
        elif amount <= 0:
            return False, "Вы указали неверную сумму для переноса"
        return [True, '']

    @staticmethod
    def validate_wax(from_key: str, steam_id: str, amount: int):
        if from_key == '':
            return False, "Вы не установили API-ключ"
        elif steam_id == '':
            return False, "Вы не установили SteamID"
        elif amount <= 0:
            return False, "Вы указали неверную сумму для переноса"
        return [True, '']

    @staticmethod
    def _hide_key(full_key: str):
        return "**************************" + full_key[len(full_key)-5:len(full_key)]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
