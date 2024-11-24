from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile
import os
import shutil


class ChadwmProfile(XorgProfile):
    def __init__(self) -> None:
        super().__init__("Chadwm", ProfileType.WindowMgr, description="")

    @property
    def packages(self) -> list[str]:
        # return super().packages + [
        return [
            "a-candy-beauty-icon-theme-git",
            "alacritty",
            "arandr",
            "arc-gtk-theme",
            "archlinux-logout-git",
            "archlinux-tweak-tool-git",
            "arcolinux-alacritty-git",
            "arcolinux-chadwm-git",
            "arcolinux-chadwm-pacman-hook-git",
            "arcolinux-nlogout-git",
            "arcolinux-powermenu-git",
            "arcolinux-wallpapers-candy-git",
            "arcolinux-wallpapers-git",
            "arconet-xfce",
            "autorandr",
            "bash-completion",
            "dash",
            "dmenu",
            "eww",
            "feh",
            "gcc",
            "git",
            "gvfs",
            "lolcat",
            "lxappearance",
            "make",
            "mkinitcpio-firmware",
            "paru-git",
            "picom",
            "polkit-gnome",
            "rofi-lbonn-wayland",
            "sxhkd",
            "thunar",
            "thunar-archive-plugin",
            "thunar-volman",
            "ttf-hack",
            "ttf-jetbrains-mono-nerd",
            "ttf-meslo-nerd-font-powerlevel10k",
            "volumeicon",
            "xfce4-notifyd",
            "xfce4-power-manager",
            "xfce4-screenshooter",
            "xfce4-settings",
            "xfce4-taskmanager",
            "xfce4-terminal",
            "xorg-xsetroot",
            "yay-git",
        ]

    @property
    def default_greeter_type(self) -> GreeterType | None:
        return GreeterType.Lightdm

    def copy_skel_to_user_home(self, username: str) -> str:
        """
        Copies the content of /etc/skel to the home directory of the specified user.

        Parameters:
            username (str): The username of the user whose home directory will be updated.

        Returns:
            str: A success or error message.
        """
        skel_path = "/etc/skel"
        home_path = os.path.expanduser(f"~{username}")

        # Check if /etc/skel exists
        if not os.path.exists(skel_path):
            return f"Error: {skel_path} does not exist."

        # Check if the user's home directory exists
        if not os.path.exists(home_path):
            return f"Error: Home directory for user '{username}' does not exist."

        try:
            # Iterate over the content of /etc/skel and copy to the user's home directory
            for item in os.listdir(skel_path):
                src = os.path.join(skel_path, item)
                dst = os.path.join(home_path, item)

                if os.path.isdir(src):
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    shutil.copy2(src, dst)

            return f"Successfully copied contents of {skel_path} to {home_path}."

        except Exception as e:
            return f"Error: {e}"
