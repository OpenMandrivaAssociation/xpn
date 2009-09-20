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
