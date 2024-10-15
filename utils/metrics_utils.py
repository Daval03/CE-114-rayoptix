import GPUtil
import seaborn as sns
import time
from datetime import timedelta
import psutil
import os

def get_gpu_usage():
    """
    Tracks the usage of the first available GPU on the system.

    Returns
    -------
    gpu_load : float or None
        The percentage of GPU load (0 to 100%). Returns None if no GPU is found.
    gpu_memory : float or None
        The amount of GPU memory used in GB. Returns None if no GPU is found.
    """
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]  # Assumes you're using the first GPU
        return gpu.load * 100, gpu.memoryUsed / 1024  # GPU load in %, memory in GB
    return None, None


def get_memory_cpu_usage():
    """
    Tracks the memory and CPU usage of the current process.

    Returns
    -------
    mem_info : float
        The amount of memory used by the current process in MB.
    cpu_usage : float
        The percentage of CPU usage by the current process.
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info().rss / (1024 * 1024)  # Memory in MB
    cpu_usage = process.cpu_percent(interval=None)  # CPU usage in percentage
    return mem_info, cpu_usage
