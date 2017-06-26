from app import emails
from app.utils import reverse


def create_invite_email(application, request):
    c = {'name': application.hacker.name,
         'confirm_url': str(reverse('confirm_app',request=request))
         }
    return emails.render_mail('register/mails/invitation', application.hacker.user.email, c)
