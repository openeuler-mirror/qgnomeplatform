Name:                qgnomeplatform
Version:             0.5
Release:             7
Summary:             The module provides Qt Theme aimed to accommodate Gnome settings
License:             LGPLv2+
URL:                 https://github.com/MartinBriza/QGnomePlatform
Source0:             https://github.com/MartinBriza/QGnomePlatform/archive/%{version}/QGnomePlatform-%{version}.tar.gz
BuildRequires:       pkgconfig(gio-2.0) pkgconfig(udev) pkgconfig(xkbcommon) gtk3-devel libinput-devel
BuildRequires:       libXrender-devel qt5-qtbase-devel qt5-qtbase-static qt5-qtbase-private-devel
Requires:            adwaita-qt5

%description
The Qt Platform Theme named QGnomePlatform which aimed to accomodate multies
GNOME settings.The utilize Qt applications without modify this them could use
the them as well as possible.

%prep
%autosetup -n  QGnomePlatform-%{version} -p1 -S git

%build
install -d %{_target_platform}
cd %{_target_platform}
%{qmake_qt5} ..
cd -
%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%doc README.md LICENSE
%{_qt5_libdir}/qt5/plugins/platformthemes/libqgnomeplatform.so

%changelog
* Tue Apr 21 2020 Jeffery.Gao <gaojianxing@huawei.com> - 0.5-7
- Package init
