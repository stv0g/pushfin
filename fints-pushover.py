import logging
from datetime import date
from fints.client import FinTS3PinTanClient
import http.client, urllib

def get_transactions(blz, iban, login, pin, start, end, endpoint):
    f = FinTS3PinTanClient(blz, login, pin, endpoint)

    accounts = f.get_sepa_accounts()

    # Find correct account
    account = [a for a in accounts where a.iban == iban]
    statement = f.get_statement(accounts[2], date(2018, 1, 1), date.today())
    
    return [t.data for t in statement]
    
    # The statement is a list of transaction objects as parsed by the mt940 parser, see
    # 
    
    # for documentation. Most information is contained in a dict accessible via their
    # ``data`` property

def send_notification(token, user, message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": token,
            "user": user,
            "message": message,
        }),
        {
            "Content-type": "application/x-www-form-urlencoded"
        }
    )
    conn.getresponse()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    trxs = get_transactions(FINTS_BLZ, FINTS_IBAN, FINTS_LOGIN, FINTS_PIN,
     start, end)

    for trx in trxs:
        msg = "".format(trx)

        send_notification(PUSHOVER_TOKEN, PUSHOVER_USER, msg)
