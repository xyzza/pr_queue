# coding: utf-8
import smtplib
from email.mime.text import MIMEText

from django.conf import settings


def send_mail(receiver, message, subject='', debug=settings.DEBUG):
    """
    :param receiver:
    :param message:
    :param debug:
    :return:
    """
    mail = MIMEText(message, _charset='utf-8')
    mail['Subject'] = u'[{1}]{0}'.format(settings.MAILPROCESSOR_SUBJECT, subject)
    mail['From'] = settings.MAILPROCESSOR_FROM
    mail['To'] = settings.MAILPROCESSOR_RECEIVER_DEBUG if debug else receiver
    # send mail
    s = smtplib.SMTP(settings.MAILPROCESSOR_SMTP_HOST)
    s.login(settings.MAILPROCESSOR_LOGIN, settings.MAILPROCESSOR_PASSWORD)
    s.sendmail(mail['From'], [mail['To'],
               settings.MAILPROCESSOR_RECEIVER_DEBUG], mail.as_string())
    s.quit()