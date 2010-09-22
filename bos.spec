%define	name	bos
%define	version 2.6.1
%define rel	1
%define	release	%mkrel %rel
%define	Summary	Invasion: Battle of survival

Name:		%{name} 
Summary:	A real time strategy game
Version:	%{version} 
Release:	%{release} 
Source0:	http://www.boswars.org/dist/releases/boswars-%{version}-src.zip
# It doesn't provide it's own icon yet
# Found this on their patch tracker
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
Patch0: 	boswars-2.5-gcc43.patch
URL:		http://www.boswars.org/
Group:		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
BuildRequires:	scons X11-devel lua-devel mesagl-devel libogg-devel
BuildRequires:	SDL-devel bzip2-devel oggvorbis-devel libmikmod-devel
BuildRequires:	libpng-devel libmng-devel
BuildRequires:  MesaGLU-devel imagemagick libtheora-devel

%description
Invasion - Battle of Survival is a real-time strategy game using
the Stratagus game engine. 

%prep
%setup -q -n boswars-%{version}-src
# %patch0 -p0 -b .gcc

%build
scons opengl=1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%_gamesbindir,%_gamesdatadir/bos}
install -m755 boswars %{buildroot}%_gamesbindir

cp -ra campaigns graphics intro languages maps scripts sounds units %{buildroot}%{_gamesdatadir}/bos/
cat << EOF > ./bos.sh
#!/bin/sh
boswars \$@ -d %{_gamesdatadir}/bos/
EOF
install -m755 ./bos.sh -D %{buildroot}%{_gamesbindir}/bos

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bos Wars
Comment=Invasion: Battle of survival - a real time strategy game
Exec=%{_gamesbindir}/bos
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;StrategyGame;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%files 
%defattr(-,root,root)
%doc doc/*
%dir %{_gamesdatadir}/bos/
%{_gamesdatadir}/bos/*
%{_gamesbindir}/bos
%{_gamesbindir}/boswars
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
