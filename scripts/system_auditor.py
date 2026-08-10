import platform
import os

print("==============================")
print("   WEEK 1 SYSTEM AUDIT REPO   ")
print("==============================")
print(f"OS Platform: {platform.system()}")
print(f"OS Release: {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"Current User: {os.getlogin() if hasattr(os, 'getlogin') else 'Unknown'}")
print("==============================")