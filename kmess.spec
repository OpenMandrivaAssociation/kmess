Name:		kmess
Version:	2.0.6.2
Release:	1
Summary:	Yet another MSN messenger for KDE
Group:		Graphical desktop/KDE
License:	GPLv2+
URL:		http://kmess.sourceforge.net
Source0:	http://ufpr.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kmess-2.0.5-linkage.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel
BuildRequires:	libgcrypt-devel
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

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

%changelog
* Thu Nov 17 2011 Sergio Rafael Lemke <sergio@mandriva.com> 2.0.6.1-2
+ Revision: 731462
- Fix unpackaged files
- Fix a problem wich makes contact list to not appear

* Wed Feb 23 2011 Sergio Rafael Lemke <sergio@mandriva.com> 2.0.6.1-0
+ Revision: 639515
- Update to version 2.0.6.1

* Mon Feb 14 2011 Funda Wang <fwang@mandriva.org> 2.0.6-3
+ Revision: 637817
- reuploaded with new tarball

* Tue Feb 08 2011 Sergio Rafael Lemke <sergio@mandriva.com> 2.0.6-2
+ Revision: 636889
- Dropped kmess-2.0.5-disableMailCheck.patch, this bug was fixed on 2.0.6, getting MailCheck functionalities back

* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 2.0.6-1
+ Revision: 636672
- add libisf-qt tarball
- update to new version 2.0.6

* Tue Jan 18 2011 Sergio Rafael Lemke <sergio@mandriva.com> 2.0.5-2
+ Revision: 631491
- Add Workarround patch to make basic Chat function work, waiting upstream bugfix release update

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2.0.5-1mdv2011.0
+ Revision: 598567
- new version 2.0.5

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 2.0.4-1mdv2011.0
+ Revision: 565302
- new version 2.0.4

* Thu Mar 11 2010 Funda Wang <fwang@mandriva.org> 2.0.3-1mdv2010.1
+ Revision: 518066
- New version 2.0.3

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.1
+ Revision: 473665
- new version 2.0.2
- new version 2.0.2

* Tue Dec 01 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.1
+ Revision: 472296
- new version 2.0.1

* Sat Oct 24 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2.0.0-2mdv2010.0
+ Revision: 459186
- Rebuild

* Sun Jul 26 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2.0.0-1mdv2010.0
+ Revision: 400232
- Update to kmess 2.0

* Fri May 15 2009 Gustavo De Nardin <gustavodn@mandriva.com> 2.0.0-0.svn4770.1mdv2010.0
+ Revision: 375872
- new version 2.0beta2

* Sat Apr 04 2009 Funda Wang <fwang@mandriva.org> 2.0.0-0.svn4516.1mdv2009.1
+ Revision: 363985
- fix static lib
- New snapshot

* Thu Feb 19 2009 Funda Wang <fwang@mandriva.org> 2.0.0-0.svn4155.1mdv2009.1
+ Revision: 342769
- New snapshot

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 2.0.0-0.svn4053.1mdv2009.1
+ Revision: 333597
- new snapshot

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 2.0.0-0.svn3479.1mdv2009.0
+ Revision: 234257
- New snapshot 3479

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 2.0.0-0.svn3247.1mdv2009.0
+ Revision: 216894
- BR xslt
- New svn snapshot 3247
- drop patch0, it is not needed any more

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Update to kmess 2  svn (ported to qt4/kde4)

* Fri Jan 11 2008 Funda Wang <fwang@mandriva.org> 1.5-1mdv2008.1
+ Revision: 147860
- New version 1.5

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 1.5-0.pre2.2mdv2008.0
+ Revision: 77296
- Remove invalid de comment of menu entry

* Thu Aug 09 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.5-0.pre2.1mdv2008.0
+ Revision: 60874
- new upstream release


* Thu Nov 23 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.5-0.pre1.1mdv2007.0
+ Revision: 86651
- Add BuildRequire
- Add sSurces
-  New version 1.5pre1
- import kmess-1.4.3-2mdk

* Fri May 12 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.3-2mdk
- Rebuild to generate categories

* Fri Apr 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.3-1mdk
- New release 1.4.3

* Mon Dec 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.1-3mdk
- Remove redundant buildRequires

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.1-2mdk
- Fix redundant buildrequires

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4.1-1mdk
- New release 1.4.1

* Sat Sep 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.4-1mdk
- New release 1.4 ( Bug fixes release )
- mkrel 
- drop patch 2 ( Merged Upstream )

* Fri Mar 11 2005 Nicolas Lecureuil <neoclust@mandrake.org> 1.3.0-1mdk
- 1.3.0
- Remove Patch 1  merged upstream
- Rediff  Patch 2

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2.1-4mdk
- Rebuild

