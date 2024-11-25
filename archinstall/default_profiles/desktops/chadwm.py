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
            "arcolinux-app-glade-git",
            "arcolinux-arc-dawn-git",
            "arcolinux-btop-git",
            "arcolinux-chadwm-nemesis-git",
            "arcolinux-chadwm-pacman-hook-git",
            "arcolinux-fastfetch-git",
            "arcolinux-hblock-git,"
            "arcolinux-nlogout-git",
            "arcolinux-powermenu-git",
            "arcolinux-wallpapers-candy-git",
            "arcolinux-wallpapers-git",
            "arconet-variety-config",
            "arconet-xfce",
            "autorandr",
            "bash-completion",
            "bat",
            "bibata-cursor-theme-bin",
            "btop",
            "dash",
            "dmenu",
            "duf",
            "eww",
            "fastfetch",
            "feh",
            "firefox",
            "gcc",
            "git",
            "gitahead-git",
            "gvfs",
            "gvfs-dnssd",
            "gvfs-smb"
            "lolcat",
            "lxappearance",
            "make",
            "meld",
            "mkinitcpio-firmware",
            "neofetch",
            "nomacs-qt6-git",
            "numlockx",
            "paru-git",
            "picom-git",
            "playerctl",
            "polkit-gnome",
            "ripgrep",
            "rofi-lbonn-wayland",
            "sublime-text-4",
            "sparklines-git",
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
            "xfce4-appfinder",
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
