Summary:	Oxyd clone
Summary(pl):	Klon gry Oxyd
Name:		enigma
Version:	0.80
Release:	0.rc1.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/%{name}/%{name}-%{version}-rc1.tar.gz
# Source0-md5:	b92e2f56b1166c693423af8932744f69
Source1:	%{name}.desktop
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
Buildrequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lua40-devel >= 4.0
URL:		http://www.freesoftware.fsf.org/enigma/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enigma is a puzzle game inspired by Oxyd on the Atari ST and
Rock'n'Roll on the Amiga: You control a small black marble and have to
find and uncover all pairs of identical Oxyd stones in each landscape.
Sounds simple? It would be, if it weren't for hidden traps, vast
mazes, insurmountable obstacles and lots of hairy puzzles, blocking
your direct way to the Oxyd stones...

%description -l pl
Enigma jest gr± logiczn± zainspirowan± przez Oxyd z Atari ST i
Rock'n'Roll z Amigi. Kontroluje siê ma³± czarn± kulkê maj±c za zadanie
odnale¼æ i odkryæ wszystkie pary identycznych kamieni Oxyd na ka¿dej
planszy. Proste? By³o by, gdyby nie ukryte pu³apki, przepastne
labirynty, niepokonane przeszkody i mnóstwo w³ochatych zagadek
blokuj±cych drogê do kamieni Oxyd.

%description -l de
Bei Enigma handelt es sich um ein Remake des 1990 erschienen
Spiele-Klassikers Oxyd. Das Ziel des Spiels ist schnell erklärt:
Versuchen Sie alle gleichfarbigen "Oxyd"-Steine in jeder Landschaft zu
finden und aufzudecken. Hört sich einfach an? Wäre es vielleicht auch,
würden nicht versteckte Fallen, gewaltige Irrgärten, scheinbar
unüberwindliche Hindernisse und viele, viele Rätsel den direkten Weg zu
den Steinen blockieren...

%prep
%setup -q -n %{name}-%{version}-rc1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	CXX="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/enigma/{fonts,sound,gfx,levels},%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_applnkdir}/Games}

install doc/enigma.6			$RPM_BUILD_ROOT%{_mandir}/man6
install src/enigma			$RPM_BUILD_ROOT%{_bindir}
install data/fonts/*.{png,txt,bmf}	$RPM_BUILD_ROOT%{_datadir}/enigma/fonts
install data/gfx/*.png			$RPM_BUILD_ROOT%{_datadir}/enigma/gfx
install data/levels/*.{lua,png,txt}	$RPM_BUILD_ROOT%{_datadir}/enigma/levels
install data/sound/*.{wav,s3m}		$RPM_BUILD_ROOT%{_datadir}/enigma/sound
install data/*.lua			$RPM_BUILD_ROOT%{_datadir}/enigma

install %{SOURCE1}		$RPM_BUILD_ROOT%{_applnkdir}/Games
install etc/enigma.png		$RPM_BUILD_ROOT%{_pixmapsdir}

rm -f doc/manual/{images,}/Makefile*
rm -f doc/manual/enigma.texi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES ChangeLog NEWS README doc/{TODO,functions.*,manual}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
