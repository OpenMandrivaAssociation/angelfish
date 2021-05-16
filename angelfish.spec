#define snapshot 20200710
#define commit 741828b3123f8b8c9e61f683fceac5a72763e237

Name:		angelfish
Version:	21.05
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Browser for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/plasma-angelfish/-/archive/v%{version}/plasma-angelfish-v%{version}.tar.bz2
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
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Purpose)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5WebEngine)

%description
Browser for Plasma Mobile

%prep
%autosetup -p1 -n angelfish-v%{version}-77d156fabe18740a53cd1894a57555e893b13eab
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/angelfish
%{_bindir}/angelfish-webapp
%{_datadir}/applications/org.kde.mobile.angelfish.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.mobile.angelfish.svg
%{_datadir}/config.kcfg/angelfishsettings.kcfg
%{_datadir}/knotifications5/angelfish.notifyrc
%{_datadir}/metainfo/org.kde.mobile.angelfish.metainfo.xml
