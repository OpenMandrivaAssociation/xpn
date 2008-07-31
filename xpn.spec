%define name	xpn
%define version	1.0.0
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	GTK2 newsreader with full Unicode support
Version: 	%{version}
Release: 	%{release}

Source:		http://ovh.dl.sourceforge.net/sourceforge/xpn/%{name}-%{version}.tar.gz
URL:		http://xpn.altervista.org/
License:	GPL
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
Requires:	gnome-python >= 2.4.1
BuildArch:	noarch

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

%install
rm -rf $RPM_BUILD_ROOT

# replace gtk.FALSE by False
perl -pi -e 's|gtk\.FALSE|False|g' xpn.py
perl -pi -e 's|gtk\.FALSE|False|g' xpn_src/*.py
# replace gtk.TRUE by True
perl -pi -e 's|gtk\.TRUE|True|g' xpn.py
perl -pi -e 's|gtk\.TRUE|True|g' xpn_src/*.py



mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/%name
mkdir -p %buildroot/%_datadir/locale
cp tags.txt %buildroot/%_datadir/%name
cp -r xpn_src %buildroot/%_datadir/%name
cp -r pixmaps %buildroot/%_datadir/%name
cp -r lang/* %buildroot/%_datadir/locale
cp %name.py %buildroot/%_datadir/%name
echo "#!/bin/bash" > %buildroot/%_bindir/%name
echo "cd %_datadir/%name" >> %buildroot/%_bindir/%name
echo "python %name.py -d \$@" >> %buildroot/%_bindir/%name
chmod 755 %buildroot/%_bindir/%name

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/%name.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/%name.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/%name.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog README TODO *.html
%attr(0755,root,root) %{_bindir}/%name
%{_datadir}/%name
%{_datadir}/locale
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
