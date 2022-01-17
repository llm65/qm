import os
import logging

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.config import conf

_FILESIZE = 20  # 单位M， 单个附件大小
_FILECOUNT = 10  # 附件个数

_smtp_cfg = conf('smtp')
_email_cfg = conf('email')

_logger = logging.getLogger('main.email1')


class Email:
    def __init__(self, subject, context=None, attachment=None):
        self.subject = subject
        self.context = context
        self.attachment = attachment

        self.message = MIMEMultipart()
        self._message_init()

    def _message_init(self):
        if self.subject:
            self.message['subject'] = Header(self.subject, 'utf-8')  # 邮件标题
        else:
            raise ValueError("Invalid subject")

        self.message['from'] = _email_cfg['sender']  # from
        self.message['to'] = _email_cfg['receivers']  # to

        if self.context:  # 正文
            self.message.attach(MIMEText(self.context, 'html1', 'utf-8'))

        if self.attachment:  # 附件
            if isinstance(self.attachment, str):  # 单个
                self._attach(self.attachment)
            if isinstance(self.attachment, list):  # 多个
                count = 0
                for each in self.attachment:
                    if count <= _FILECOUNT:  # 数量上限
                        self._attach(each)
                        count += 1
                    else:
                        _logger.warning('Attachments is more than ', _FILECOUNT)
                        break

    def _attach(self, file):  # 附件
        if os.path.isfile(file) and os.path.getsize(file) <= _FILESIZE * 1024 * 1024:  # 大小限制
            # MIMEApplication：客户端根据文件扩展名来猜测文件类型
            attach = MIMEApplication(open(file, 'rb').read())  # 2进制文件
            attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))  # 附件名
            attach["Content-Type"] = 'application/octet-stream'  # 文件类型

            self.message.attach(attach)
        else:
            _logger.error('The attachment is not exist or more than %sM: %s' % (_FILESIZE, file))

    def send_mail(self):
        s = smtplib.SMTP_SSL(_smtp_cfg['host'], int(_smtp_cfg['port']))
        result = True
        try:
            s.login(_smtp_cfg['user'], _smtp_cfg['passwd'])
            s.send_message(self.message)
        except smtplib.SMTPException:
            result = False
            _logger.error('Send mail failed', exc_info=True)
        finally:
            s.close()
        return result


if __name__ == '__main__':
    Email('标题', '正文', '附件.png').send_mail()
