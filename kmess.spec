%define name	 kmess
%define version	 2.0.0
%define release	 %mkrel 0.svn%{svn}.1
%define svn      2898 

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Graphical desktop/KDE
License:	GPLv2+
Source0:        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.svn%{svn}.tar.bz2
Patch0:		kmess-1.5pre2-remove-de-comment.patch
URL:		http://kmess.sourceforge.net
BuildRequires:  kdebase4-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Summary:	Yet another MSN messenger for KDE


%description
KMess is an easy-to-use MSN Messenger client for KDE. Install it
if you want an MSN Messenger client.

%files
%defattr(-,root,root)
%doc %{_kde_docdir}/HTML/*/%{name}
%doc AUTHORS INSTALL TODO README ChangeLog
%{_kde_bindir}/%{name}
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/applications/kde4/kmess.desktop
%{_kde_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_kde_iconsdir}/hicolor/22x22/apps/kmess.png
%{_kde_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_kde_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_kde_iconsdir}/hicolor/64x64/apps/kmess.png
%{_kde_iconsdir}/hicolor/128x128/apps/kmess.png
%{_kde_iconsdir}/locolor/16x16/apps/%{name}.png
%{_kde_iconsdir}/locolor/22x22/apps/kmess.png
%{_kde_iconsdir}/locolor/32x32/apps/%{name}.png
%dir %{_kde_datadir}/emoticons/KMess-new
%{_kde_datadir}/emoticons/KMess-new/*.png
%{_kde_datadir}/emoticons/KMess-new/emoticons.xml
%{_kde_datadir}/sounds/%{name}*.ogg
#FIXME : Remove when kde4 will be on /
%{_kde_datadir}/locale/*/LC_MESSAGES/*.mo

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p0


%build
%cmake_kde4

%make

%install
rm -rf $RPM_BUILD_ROOT
cd build 
%makeinstall_std
#install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
#install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
#install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

#Relativisation of symlink, rpm fails to do it
#rm -f $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/%{name}/common
#ln -sf ../common $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/%{name}/common

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT
