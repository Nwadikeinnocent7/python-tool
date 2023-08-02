import subprocess
import datetime

def get_installed_packages():
    package_list_cmd = "apt list --installed 2>/dev/null | grep -v 'Listing...'"
    
    try:
        package_info = subprocess.check_output(package_list_cmd, shell=True, text=True)
        return parse_package_info(package_info)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def parse_package_info(package_info):
    packages = []
    for line in package_info.splitlines():
        package, version = line.strip().split("/")
        install_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        packages.append({"package": package, "version": version, "install_time": install_time})
    return packages

def list_installed_packages():
    packages = get_installed_packages()
    if packages:
        print("Installed Linux packages:")
        for package in packages:
            print(f"{package['package']} - {package['version']} (Installed on: {package['install_time']})")
    else:
        print("Failed to retrieve installed packages.")

if __name__ == "__main__":
    list_installed_packages()
