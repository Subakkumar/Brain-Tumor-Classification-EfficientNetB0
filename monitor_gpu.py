"""
GPU Performance Monitor for Brain Tumor Classification
Run this in a separate terminal to monitor GPU usage during training
"""

import time
import subprocess
import psutil
import GPUtil

def monitor_system():
    """Monitor GPU and system resources"""
    try:
        # Get GPU information
        gpus = GPUtil.getGPUs()
        
        print("\n" + "="*60)
        print("🧠 BRAIN TUMOR CLASSIFICATION - GPU MONITOR")
        print("="*60)
        
        # GPU Info
        if gpus:
            for gpu in gpus:
                print(f"🎯 GPU: {gpu.name}")
                print(f"   Load: {gpu.load*100:.1f}%")
                print(f"   Memory: {gpu.memoryUsed}MB / {gpu.memoryTotal}MB ({gpu.memoryUtil*100:.1f}%)")
                print(f"   Temperature: {gpu.temperature}°C")
        else:
            print("❌ No GPU detected")
        
        # CPU and Memory
        print(f"\n💻 CPU Usage: {psutil.cpu_percent()}%")
        memory = psutil.virtual_memory()
        print(f"🧠 Memory Usage: {memory.used//(1024**3)}GB / {memory.total//(1024**3)}GB ({memory.percent}%)")
        
        # Disk usage
        disk = psutil.disk_usage('/')
        print(f"💾 Disk Usage: {disk.used//(1024**3)}GB / {disk.total//(1024**3)}GB ({disk.percent}%)")
        
    except Exception as e:
        print(f"⚠️  Monitoring error: {e}")

if __name__ == "__main__":
    print("Starting GPU monitoring... (Press Ctrl+C to stop)")
    try:
        while True:
            monitor_system()
            time.sleep(5)  # Update every 5 seconds
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped")