Summary:	Yet another MSN messenger for KDE
Name:		kmess
Version:	2.0.6.2
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kmess.sourceforge.net
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kmess-2.0.5-linkage.patch
Patch1:		kmess-2.0.6.2-fix-crash-in-contactlistmodel.patch
Patch2:		kmess-2.0.6.2-giflib51.patch
BuildRequires:	giflib-devel
BuildRequires:	kdebase4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(xscrnsaver)

%description
KMess is an easy-to-use MSN Messenger client for KDE. Install it
if you want an MSN Messenger client.

%files -f %{name}.lang
%doc AUTHORS INSTALL TODO README ChangeLog
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_datadir}/apps/%{name}
%{_kde_configdir}/*.knsrc
%{_kde_datadir}/applications/kde4/kmess.desktop
%{_kde_iconsdir}/*/*/apps/%{name}.*
%dir %{_kde_datadir}/emoticons/KMess-new
%{_kde_datadir}/emoticons/KMess-new/*.png
%{_kde_datadir}/emoticons/KMess-new/emoticons.xml
%{_kde_datadir}/sounds/%{name}*.ogg

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

