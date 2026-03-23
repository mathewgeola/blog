import argparse
import os
import platform
import re
import subprocess

GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"


class AAPT2NotFoundError(Exception):
    pass


def get_aapt2_path() -> str:
    system = platform.system()

    if system == "Windows":
        base_paths = [
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Android", "Sdk"),
        ]
        exe_name = "aapt2.exe"

    elif system == "Darwin":
        base_paths = [
            os.path.expanduser("~/Library/Android/sdk"),
        ]
        exe_name = "aapt2"

    elif system == "Linux":
        base_paths = [
            os.path.expanduser("~/Android/Sdk"),
        ]
        exe_name = "aapt2"

    else:
        raise AAPT2NotFoundError(f"不支持的系统: {system}")

    for sdk_path in base_paths:
        build_tools_dir = os.path.join(sdk_path, "build-tools")

        if not os.path.isdir(build_tools_dir):
            continue

        versions = sorted(os.listdir(build_tools_dir), reverse=True)

        for version in versions:
            aapt2_path = os.path.join(build_tools_dir, version, exe_name)
            if os.path.isfile(aapt2_path):
                return aapt2_path

    raise AAPT2NotFoundError("未找到 aapt2，请确认已安装 Android SDK Build-Tools")


def rename_apk(file_path: str) -> None:
    dir_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    if file_path.endswith(".apk"):
        print(file_name, end="")

        env = os.environ.copy()
        aapt2_path = get_aapt2_path()
        aapt2_dir = os.path.dirname(aapt2_path)
        env["PATH"] = aapt2_dir + os.pathsep + env.get("PATH", "")

        process = subprocess.Popen([
            "aapt2",
            "dump",
            "badging",
            file_path,
        ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            env=env
        )

        apk_info = dict()

        for line in iter(process.stdout.readline, ""):
            if (key1 := "package") in line:
                if ret := re.findall(rf"\b{key1}:(.*)", line, re.DOTALL):
                    if (key2 := "name") in ret[0]:
                        if ret2 := re.findall(rf"\b{key2}='(.*?)'", line, re.DOTALL):
                            apk_info[" ".join([key1, key2])] = ret2[0]
                    if (key2 := "versionName") in ret[0]:
                        if ret2 := re.findall(rf"\b{key2}='(.*?)'", line, re.DOTALL):
                            apk_info[" ".join([key1, key2])] = ret2[0]

            if (key := "application-label") in line:
                if ret := re.findall(rf"\b{key}:'(.*?)'", line, re.DOTALL):
                    apk_info[key] = ret[0]

            if (key := "application-label-zh") in line:
                if ret := re.findall(rf"\b{key}:'(.*?)'", line, re.DOTALL):
                    apk_info[key] = ret[0]

            if (key := "application-label-zh-CN") in line:
                if ret := re.findall(rf"\b{key}:'(.*?)'", line, re.DOTALL):
                    apk_info[key] = ret[0]

        application_label = apk_info.get("application-label")
        if value := apk_info.get("application-label-zh"):
            application_label = value
        if value := apk_info.get("application-label-zh-CN"):
            application_label = value

        package_version_name = apk_info.get("package versionName")

        if application_label and package_version_name:
            new_file_name = application_label + "_" + package_version_name + ".apk"

            if new_file_name != file_name:
                new_file_path = os.path.join(dir_path, new_file_name)
                os.rename(file_path, new_file_path)
                print(f"{GREEN} ==> {new_file_name}{RESET}", end="\n")
                return
            else:
                print(f"{BLUE} ==> {new_file_name}{RESET}", end="\n")
                return

        print(f"{RED} ==> X{RESET}", end="\n")
        return


def rename_apks(dir_path: str) -> None:
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            rename_apk(file_path)


if __name__ == '__main__':
    def main():
        parser = argparse.ArgumentParser(description="rename_apk")

        parser.add_argument("-f", "--file_path", type=str, help="input file_path")
        parser.add_argument("-d", "--dir_path", type=str, help="input dir_path (default: current working directory)")

        args = parser.parse_args()

        if file_path := args.file_path:
            rename_apk(file_path)

        if not (dir_path := args.dir_path):
            dir_path = os.path.dirname(os.path.abspath(__file__))
        rename_apks(dir_path)


    main()
