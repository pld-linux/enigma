Summary:	Oxyd clone
Summary(pl):	Klon gry Oxyd
Name:		enigma
Version:	0.40a
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/enigma/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lua-devel >= 4.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
URL:		http://www.freesoftware.fsf.org/enigma/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd. Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape. Sounds simple? It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

So far, Enigma implements about 80% of the game engine and a couple of
simple objects, but a great deal is still missing. In particular, the
game currently lacks game objects, graphics and sound effects, and,
most importantly, the 200 levels that made Oxyd so entertaining.

%description -l pl
Enigma jest ho³dem dla i reimplementacj± jednej z najoryginalniejszych
i najbardziej intryguj±cych gier komputerowych lat
dziewiêædziesi±tych, Oxyd. Zadanie jest proste: znajd¼ i odkryj
wszystkie pary identycznych Oxydowych kamieni na ka¿dej planszy. Brzmi
³atwo? Tak by by³o, gdyby nie ukryte pu³apki, obszerne labirynty,
niepokonane przeszkody i niezliczone ³amig³ówki blokuj±ce drogê do
Oxydowych kamieni...

Jak na razie Enigma implementuje oko³o 80% silnika gry i kilka
prostych obiektów, lecz wiele rzeczy jeszcze brakuje, szczególnie
obiektów, grafiki, efektów d¼wiêkowych, i, co najwa¿niejsze, 200
poziomów dziêki którym Oxyd by³ tak przyjemny.

%prep
%setup -q

%build
aclocal
autoheader
%{__autoconf}
%{__automake}

%configure \
	CXX="%{__cxx}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/enigma/{fonts,sound,gfx,levels},%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_applnkdir}/Games}

install enigma.6		$RPM_BUILD_ROOT%{_mandir}/man6
install enigma			$RPM_BUILD_ROOT%{_bindir}
install fonts/*.{png,txt,bmf}	$RPM_BUILD_ROOT%{_datadir}/enigma/fonts
install gfx/*.png		$RPM_BUILD_ROOT%{_datadir}/enigma/gfx
install levels/*.{lua,png}	$RPM_BUILD_ROOT%{_datadir}/enigma/levels
install sound/*.{wav,s3m}	$RPM_BUILD_ROOT%{_datadir}/enigma/sound
install *.lua			$RPM_BUILD_ROOT%{_datadir}/enigma

install %{SOURCE1}		$RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2}		$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/enigma
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
