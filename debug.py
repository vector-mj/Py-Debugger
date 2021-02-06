import my_debug
debugger = my_debug.debugger()
pid = input("Enter the PID of the process to attach to: ")
debugger.attach(int(pid))
debugger.detach()