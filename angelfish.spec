#define snapshot 20200710
#define commit 741828b3123f8b8c9e61f683fceac5a72763e237

Name:		angelfish
Version:	22.02
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Browser for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/plasma-angelfish/-/archive/v%{version}/plasma-angelfish-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Feedback)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Purpose)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(Qt5WebEngine)

%description
Browser for Plasma Mobile

%prep
%if 0%{?snapshot}
%autosetup -p1 -n angelfish-v%{version}-77d156fabe18740a53cd1894a57555e893b13eab
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/angelfish
%{_bindir}/angelfish-webapp
%{_datadir}/config.kcfg/angelfishsettings.kcfg
%{_datadir}/knotifications5/angelfish.notifyrc
%{_datadir}/applications/org.kde.angelfish.desktop
%{_datadir}/icons/hicolor/*/*/org.kde.angelfish.svg
%{_datadir}/metainfo/org.kde.angelfish.metainfo.xml
