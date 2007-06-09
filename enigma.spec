Summary:	Oxyd clone
Summary(pl.UTF-8):	Klon gry Oxyd
Name:		enigma
Version:	1.01
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/enigma-game/%{name}-%{version}.tar.gz
# Source0-md5:	d3804534ac03425051ebfd383ed1b4ee
Source1:	%{name}.desktop
URL:		http://www.nongnu.org/enigma/
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xerces-c-devel >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enigma is a puzzle game inspired by Oxyd on the Atari ST and
Rock'n'Roll on the Amiga: You control a small black marble and have to
find and uncover all pairs of identical Oxyd stones in each landscape.
Sounds simple? It would be, if it weren't for hidden traps, vast
mazes, insurmountable obstacles and lots of hairy puzzles, blocking
your direct way to the Oxyd stones...

%description -l de.UTF-8
Bei Enigma handelt es sich um ein Remake des 1990 erschienen
Spiele-Klassikers Oxyd. Das Ziel des Spiels ist schnell erklärt:
Versuchen Sie alle gleichfarbigen "Oxyd"-Steine in jeder Landschaft zu
finden und aufzudecken. Hört sich einfach an? Wäre es vielleicht auch,
würden nicht versteckte Fallen, gewaltige Irrgärten, scheinbar
unüberwindliche Hindernisse und viele, viele Rätsel den direkten Weg zu
den Steinen blockieren...

%description -l pl.UTF-8
Enigma jest grą logiczną zainspirowaną przez Oxyd z Atari ST i
Rock'n'Roll z Amigi. Kontroluje się małą czarną kulkę mając za zadanie
odnaleźć i odkryć wszystkie pary identycznych kamieni Oxyd na każdej
planszy. Proste? Było by, gdyby nie ukryte pułapki, przepastne
labirynty, niepokonane przeszkody i mnóstwo włochatych zagadek
blokujących drogę do kamieni Oxyd.

%prep
%setup -q

# hack: don't rebuild it, requires too new(?) version of texi2html
# (doesn't work with texi2html 1.56k from tetex 2.0.2)
touch doc/manual/*.html

%build
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
 
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1}			$RPM_BUILD_ROOT%{_desktopdir}
install data/gfx/enigma_marble.png	$RPM_BUILD_ROOT%{_pixmapsdir}/enigma.png

rm -f doc/manual/{images,}/Makefile*
rm -f doc/manual/enigma.texi

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README doc/manual
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man6/*
%{_pixmapsdir}/*
