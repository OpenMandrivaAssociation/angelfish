%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit 741828b3123f8b8c9e61f683fceac6a72763e237

Name:		plasma6-angelfish
Version:	24.02.1
Release:	%{?git:0.%{git}.}1
Summary:	Browser for Plasma Mobile
Url:		https://invent.kde.org/network/angelfish
%if 0%{?git}
Source0:	https://invent.kde.org/network/angelfish/-/archive/%{gitbranch}/angelfish-%{gitbranchd}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/angelfish-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
#BuildRequires:	cmake(Qt6Feedback)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(FutureSQL6)
BuildRequires:	cmake(QCoro6)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qtbase-sql-postgresql
BuildRequires:	qt6-qtbase-sql-odbc
BuildRequires:	qt6-qtbase-sql-mariadb
BuildRequires:	qt6-qtbase-sql-firebird

%description
Browser for Plasma Mobile

%prep
%autosetup -p1 -n angelfish-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang angelfish

%files -f angelfish.lang
%{_bindir}/angelfish
%{_bindir}/angelfish-webapp
%{_datadir}/config.kcfg/angelfishsettings.kcfg
%{_datadir}/knotifications6/angelfish.notifyrc
%{_datadir}/applications/org.kde.angelfish.desktop
%{_datadir}/icons/hicolor/*/*/org.kde.angelfish.svg
%{_datadir}/metainfo/org.kde.angelfish.metainfo.xml
