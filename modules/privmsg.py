from core.response_codes import *

def init():
    add_hook('PRIVMSG', lambda origin, args: transmit('PRIVMSG', origin, args))
    add_hook('NOTICE', lambda origin, args: transmit('NOTICE', origin, args))

def transmit(method, origin, args):
    if len(args) < 2:
        origin.message(server.host, ERR_NEEDMOREPARAMS, method, "Not enough parameters")
        return
    if args[0][0] in '#':
        return # Not our problem.
    target = m('user_manager').get_user(args[0])
    if target is None:
        origin.message(server.host, ERR_NOSUCHNICK, args[0], "No such nick/channel")
    target.message("%s!%s@%s" % (origin.nick, origin.user, origin.host), method, args[0], args[1])
