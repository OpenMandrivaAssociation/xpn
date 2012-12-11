Name: 	 		xpn
Version: 		1.2.6
Release: 		%mkrel 2

Summary:	GTK2 newsreader with full Unicode support
License:	GPLv2+
Group:		Networking/News
URL:		http://xpn.altervista.org/
Source0:	http://xpn.altervista.org/codice/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	gnome-python >= 2.4.1

%description
With XPN you can read/write articles on the Usenet with a good MIME support
(better than some well known newsreaders).

XPN can operate with all the most diffuse charset starting from US-ASCII to
UTF-8. When you edit an article XPN automatically chooses the best charset,
however is always possible to override this choice.

There also other useful features like scoring, filtered views, random
tag-lines, external editor support, one-key navigation, ROT13, spoiler char ...

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/locale
cp tags.txt %{buildroot}/%{_datadir}/%{name}
cp -r xpn_src %{buildroot}/%{_datadir}/%{name}
cp -r pixmaps %{buildroot}/%{_datadir}/%{name}
cp -r lang/{de,fr,it} %{buildroot}/%{_datadir}/locale
cp %{name}.py %{buildroot}/%{_datadir}/%{name}

#wrapper
cat<<EOF>%{buildroot}/%{_bindir}/%{name}
#!/bin/bash
cd %{_datadir}/%{name}
python %{name}.py -d \$@
EOF
chmod 755 %{buildroot}/%{_bindir}/%{name}

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Internet-News;Network;News;
EOF

#icons
mkdir -p %{buildroot}/%{_liconsdir}
convert -size 48x48 pixmaps/%{name}.xpm %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert -size 32x32 pixmaps/%{name}.xpm %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 16x16 pixmaps/%{name}.xpm %{buildroot}/%{_miconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus

%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog README TODO *.html
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2.6-2mdv2010.0
+ Revision: 446265
- rebuild

* Sun Feb 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.6-1mdv2009.1
+ Revision: 336202
- update to new version 1.2.6

* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 1.2.5-1mdv2009.1
+ Revision: 328708
- Release 1.2.5

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-4mdv2009.0
+ Revision: 262701
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-3mdv2009.0
+ Revision: 257687
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 04 2008 Guillaume Bedot <littletux@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 178928
- 1.0.0

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 18 2007 Guillaume Bedot <littletux@mandriva.org> 0.7.0-1mdv2008.0
+ Revision: 14699
- New release 0.7.0


* Sun Sep 10 2006 Emmanuel Andry <eandry@mandriva.org> 0.5.6-3mdv2007.0
- xdg menu (#25479)

* Sun May 07 2006 Guillaume Bedot <littletux@mandriva.org> 0.5.6-2mdk
- Wrapper fix
- Do install translations + tags.txt

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.6-1mdk
- New release 0.5.6
- Fix Source URL to make it rpmbuildupdate friendly
- use mkrel

* Wed Jul 27 2005 Lenny Cartier <lenny@mandriva.com> 0.4.0-4mdk
- back to 0.4.0
- use False|True rather than gtk.FALSE|gtk.TRUE

* Wed Jan 26 2005 Austin Acton <austin@mandrake.org> 0.4.0-3mdk
- fix menu entry
- system wide install thanks to Python Hacker Guillaume Bedot

* Tue Jan 25 2005 Austin Acton <austin@mandrake.org> 0.4.0-2mdk
- oops, fix startup script

* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.4.0-1mdk
- initial package

