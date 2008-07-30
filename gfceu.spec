Summary: GFCE Ultra Nintendo Emulator frontend 
Name: gfceu
Version: 0.6.0
Release: 3%{?dist}
License: GPLv2+
Group: Applications/Emulators
URL: http://dietschnitzel.com/gfceu/
Source: http://dietschnitzel.com/gfceu/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: pygtk2-libglade 
Requires: alsa-oss
Requires: fceultra
Requires: hicolor-icon-theme

%description
GFCE Ultra is an intuitive interface for the popular Nintendo Emulator, 
FCE Ultra. It is designed for the GNOME desktop, and allows the user to 
easily play NES ROM images. Gfceu sports a number of features, including: 

* Network play
* Custom input configuration
* Fullscreen support
* OpenGL support
* Sound support
* High compatibility, accurate emulation, and all the power of FCE Ultra!

GNOME FCE Ultra is developed and maintained by Lukas Sabota.

%prep
%setup -q

# Fix .desktop file Categories
sed -i 's/GNOME;GTK;Game;/Game;Emulator;/' %{name}.desktop

# Patch to run fceultra instead of fceu
sed -i 's/'\''fceu'\''/'\''fceultra'\''/' gfceu

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 gfceu %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -m 644 {gfceu.glade,gfceu.png,gfceu_big.png} %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -m 644 gfceu.1 %{buildroot}%{_mandir}/man1

# install desktop file and icon
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{name}.desktop
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p %{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root)
%{_bindir}/gfceu
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_datadir}/applications/dribble-%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%doc ChangeLog COPYING TODO

%changelog
* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.6.0-3
- rebuild for buildsys cflags issue

* Fri Nov 02 2007 Andrea Musuruane <musuruan@gmail.com> 0.6.0-2
- Changed license due to new guidelines
- Removed %%{?dist} tag from changelog
- Updated icon cache scriptlets to be compliant to new guidelines

* Thu Mar 01 2007 Andrea Musuruane <musuruan@gmail.com> 0.6.0-1
- Updated to latest 0.6.0.
- Added now required alsa-oss to BR
- Updated URL and Source tag.
- Dropped dribble-menus Requires.
- Dropped --add-category X-Fedora from desktop-file-install.
- Dropped .desktop file patch. Now using sed.
- fceu has been renamed to fceultra to avoid conflicts (Dribble #77).

* Mon Oct 23 2006 Andrea Musuruane <musuruan@gmail.com> 0.5.2-2
- Added hicolor-icon-theme to Requires.
- Package fceu has been renamed fceultra. Changed the Requires tag accorgingly.

* Sat Oct 21 2006 Andrea Musuruane <musuruan@gmail.com> 0.5.2-1
- First release for Dribble based on mde RPM
- Updated to 0.5.2

* Mon Aug 28 2006 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.5-1
- Rebuild for mde

