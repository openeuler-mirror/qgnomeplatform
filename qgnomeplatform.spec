Name:                qgnomeplatform
Version:             0.5
Release:             10
Summary:             The module provides Qt Theme aimed to accommodate Gnome settings
License:             LGPLv2+
URL:                 https://github.com/MartinBriza/QGnomePlatform
Source0:             https://github.com/MartinBriza/QGnomePlatform/archive/%{version}/QGnomePlatform-%{version}.tar.gz
BuildRequires:       pkgconfig(gio-2.0) pkgconfig(udev) pkgconfig(xkbcommon) gtk3-devel libinput-devel
BuildRequires:       libXrender-devel qt5-qtbase-devel qt5-qtbase-static qt5-qtbase-private-devel
Requires:            adwaita-qt5
Patch0:              fix-cxx.patch

%description
The Qt Platform Theme named QGnomePlatform which aimed to accomodate multies
GNOME settings.The utilize Qt applications without modify this them could use
the them as well as possible.

%prep
%autosetup -n QGnomePlatform-%{version} -p1

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
* Thu Apr 27 2023 yoo <sunyuechi@iscas.ac.cn> - 0.5-10
- Add support for specifying cxx

* Sat Jul 31 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.5-9
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Mon May 31 2021 huanghaitao <huanghaitao8@huawei.com> - 0.5-8
- Completing build dependencies to fix git commands missing error

* Tue Apr 21 2020 Jeffery.Gao <gaojianxing@huawei.com> - 0.5-7
- Package init
