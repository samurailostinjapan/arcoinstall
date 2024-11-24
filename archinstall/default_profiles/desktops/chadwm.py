from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


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
            "arcolinux-arc-dawn-git",
            "arcolinux-chadwm-nemesis-git",
            "arcolinux-chadwm-pacman-hook-git",
            "arcolinux-nlogout-git",
            "arcolinux-powermenu-git",
            "arcolinux-wallpapers-candy-git",
            "arcolinux-wallpapers-git",
            "arconet-variety-config",
            "arconet-xfce",
            "autorandr",
            "bash-completion",
            "bibata-cursor-theme-bin",
            "dash",
            "dmenu",
            "eww",
            "fastfetch",
            "firefox",
            "feh",
            "gcc",
            "git",
            "gvfs",
            "gvfs-dnssd",
            "lolcat",
            "lxappearance",
            "make",
            "meld",
            "mkinitcpio-firmware",
            "neofetch",
            "paru-git",
            "picom-git",
            "polkit-gnome",
            "ripgrep",
            "rofi-lbonn-wayland",
            "sublime-text-4",
            "sxhkd",
            "thunar",
            "thunar-archive-plugin",
            "thunar-volman",
            "ttf-hack",
            "ttf-jetbrains-mono-nerd",
            "ttf-meslo-nerd-font-powerlevel10k",
            "variety",
            "volumeicon",
            "xdg-desktop-portal",
            "xdg-user-dirs",
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
