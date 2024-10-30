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

def get_disk_usage():
    """
    Tracks disk read and write usage of the current process.

    Returns
    -------
    read_bytes : float
        The number of bytes read from disk by the current process.
    write_bytes : float
        The number of bytes written to disk by the current process.
    """
    process = psutil.Process(os.getpid())
    io_counters = process.io_counters()
    read_bytes = io_counters.read_bytes / (1024 * 1024)  # Convert to MB
    write_bytes = io_counters.write_bytes / (1024 * 1024)  # Convert to MB
    return read_bytes, write_bytes

def get_memory_bandwidth():
    """
    Tracks the memory bandwidth usage (used and available rates).

    Returns
    -------
    memory_used : float
        The memory used rate in MB.
    memory_available : float
        The memory available rate in MB.
    """
    memory_info = psutil.virtual_memory()
    memory_used = memory_info.used / (1024 * 1024)  # Convert to MB
    memory_available = memory_info.available / (1024 * 1024)  # Convert to MB
    return memory_used, memory_available

def get_temperature_info():
    """
    Tracks the temperature of system components (CPU, GPU).

    Returns
    -------
    temperatures : dict
        A dictionary with temperature information for various components (if available).
    """
    try:
        temp_info = psutil.sensors_temperatures()
        if temp_info:
            return {sensor: temps[0].current for sensor, temps in temp_info.items()}
        else:
            return {}
    except Exception as e:
        return {"error": str(e)}

def get_cpu_frequency():
    """
    Tracks the CPU frequency.

    Returns
    -------
    current_freq : float
        The current CPU frequency in MHz.
    max_freq : float
        The maximum CPU frequency in MHz.
    """
    cpu_freq = psutil.cpu_freq()
    if cpu_freq:
        return cpu_freq.current, cpu_freq.max
    return None, None

def get_cache_memory_usage():
    """
    Tracks the cache memory usage of the system.

    Returns
    -------
    cache_memory : float
        The amount of cache memory used in MB. Returns 0 if not available.
    """
    virtual_mem = psutil.virtual_memory()
    cache_memory = getattr(virtual_mem, 'cached', 0) / (1024 * 1024)  # Convert to MB
    return cache_memory


def get_swap_memory_usage():
    """
    Tracks the swap memory usage of the system.

    Returns
    -------
    swap_memory : float
        The amount of swap memory used in MB.
    """
    swap_mem = psutil.swap_memory()
    swap_memory = swap_mem.used / (1024 * 1024)  # Convert to MB
    return swap_memory
