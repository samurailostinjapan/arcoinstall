from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class ChadwmProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Chadwm', ProfileType.WindowMgr, description='')

	@property
	def packages(self) -> list[str]:
		# return super().packages + [
		return [
		    'a-candy-beauty-icon-theme-git',
		    'alacritty',
		    'archlinux-logout-git',
		    'archlinux-tweak-tool-git',
		    'arcolinux-alacritty-git',
		    'arcolinux-chadwm-git',
		    'arcolinux-chadwm-pacman-hook-git',
		    'arcolinux-nlogout-git',
		    'arcolinux-powermenu-git',
		    'arcolinux-wallpapers-candy-git',
		    'arcolinux-wallpapers-git',
		    'arconet-xfce',
		    'arc-gtk-theme',
		    'autorandr',
		    'arandr',
		    'bash-completion',
		    'dash',
		    'dmenu',
		    'eww',
		    'feh',
		    'gcc',
		    'gvfs',
		    'lolcat',
		    'lxappearance',
		    'make',
		    'picom',
		    'polkit-gnome',
		    'rofi-lbonn-wayland',
		    'sxhkd',
		    'thunar',
		    'thunar-archive-plugin',
		    'thunar-volman',
		    'ttf-hack',
		    'ttf-jetbrains-mono-nerd',
		    'ttf-meslo-nerd-font-powerlevel10k',
		    'volumeicon',
		    'xfce4-notifyd',
		    'xfce4-power-manager',
		    'xfce4-screenshooter',
		    'xfce4-settings',
		    'xfce4-taskmanager',
		    'xfce4-terminal',
		    'xorg-xsetroot',
		]

	@property
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Lightdm

