import PAM
version = (0, 0, 1)

class PamAuthenticatorPlugin(object):
    def __init__(self, service='passwd'):
        self.service = service

    def authenticate(self, environ, identity):
        try:
            login = identity['login']
            password = identity['password']
        except KeyError:
            return None

        def pam_conv(auth, query_list, userData):
            resp = []
            for i in range(len(query_list)):
                query, type = query_list[i]
                if type == PAM.PAM_PROMPT_ECHO_OFF:
                    resp.append((password, 0))
                else:
                    return None
            return resp

        auth = PAM.pam()
        auth.start(self.service)
        auth.set_item(PAM.PAM_USER, login)
        auth.set_item(PAM.PAM_CONV, pam_conv)

        try:
            auth.authenticate()
            auth.acct_mgmt()
        except PAM.error, resp:
            return None
        except:
            raise
        else:
            return login

if __name__ == '__main__':
    from getpass import getpass
    a = PamAuthenticatorPlugin()
    user = raw_input("User: ")
    password = getpass()
    print a.authenticate({}, {'login': user, 'password': password})
