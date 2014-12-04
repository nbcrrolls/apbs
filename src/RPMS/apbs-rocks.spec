## ###########################################################################
## $Id: apbs-rocks.spec,v 1.24 2012/07/05 21:45:53 rok Exp $
## $Source: /home/rok/src/cvsroot/apbs-roll/src/RPMS/apbs-rocks.spec,v $
##
## File:    $RCSfile: apbs-rocks.spec,v $
##
## Purpose: Spec file for building RPMS for Rocks APBS-Roll
##
##          rpmbuild -ba apbs-rocks.spec
##
## Author:  Robert Konecny
## ###########################################################################

%define _topdir ZZZBUILDROOTZZZ
%define apbs_version ZZZVERSIONZZZ
%define apbs_rel 2
%define rpm_name apbs-rocks
%define buildroot %{_topdir}/%{rpm_name}-%{apbs_version}-root


# must be defined: $MPI_DIR and $MKLPATH

Name: %{rpm_name}
Summary: Adaptive Poisson Boltzmann Solver
Version: %{apbs_version}
Release: %{apbs_rel}
License: GPL
Group: Applications/Science
Vendor: Baker Research Group, PNNL / NBCR
Packager: Robert Konecny <rok@ucsd.edu>
URL: http://www.poissonboltzmann.org/apbs/
Prefix: /opt/apbs-%{apbs_version}
Buildroot: %{buildroot}
Requires: coreutils
# apbs: http://sourceforge.net/projects/apbs
Source: apbs-%{apbs_version}-source.tar.gz

%description
APBS is a software package for the numerical solution of the Poisson-Boltzmann 
equation (PBE), one of the most popular continuum models for describing 
electrostatic interactions between molecular solutes in salty, aqueous media. 
Continuum electrostatics plays an important role in several areas of 
biomolecular simulation, including:

    * simulation of diffusional processes to determine ligand-protein and 
        protein-protein binding kinetics,
    * implicit solvent molecular dynamics of biomolecules ,
    * solvation and binding energy calculations to determine ligand-protein 
        and protein-protein equilibrium binding constants and aid in rational 
        drug design,
    * and biomolecular titration studies. 

APBS was designed to efficiently evaluate electrostatic properties for such 
simulations for a wide range of length scales to enable the investigation of 
molecules with tens to millions of atoms.

This software was primarily by written Nathan Baker during his graduate work 
with J. Andrew McCammon and Michael Holst and enhanced by contributions from 
several other authors. 

%prep

%setup -q -c -T -a 0

%build

arch=%_arch
host=%_host
echo "Buidling for: arch: ${arch}, host: ${host}"

# parallel
pushd apbs-%{version}-source
export CPPFLAGS="-I/opt/openmpi/include"
export LDFLAGS="-static -L/opt/openmpi/lib -lmpi"
MPI_DIR=/opt/openmpi
#./configure --prefix=${RPM_BUILD_ROOT}/%{prefix} --with-openmpi=${MPI_DIR}
./configure --with-openmpi=${MPI_DIR}
make
popd

%install
##mkdir -p ${RPM_BUILD_ROOT}/%{prefix}

# apbs install
pushd apbs-%{version}-source
#make install
make install prefix=$RPM_BUILD_ROOT/%{prefix}
#mv ${RPM_BUILD_ROOT}/%{prefix}/bin/apbs ${RPM_BUILD_ROOT}/%{prefix}/bin/apbs.p
popd
#pushd apbs-%{version}-source-serial
#make install
#mv ${RPM_BUILD_ROOT}/%{prefix}/bin/apbs ${RPM_BUILD_ROOT}/%{prefix}/bin/apbs.serial
#mv ${RPM_BUILD_ROOT}/%{prefix}/bin/apbs.p ${RPM_BUILD_ROOT}/%{prefix}/bin/apbs
#popd

%clean
rm -rf ${RPM_BUILD_ROOT}
rm -rf ${RPM_BUILD_DIR}/%{name}-%{version}

%post
/bin/ln -fs %{prefix} /opt/apbs

%postun
rm -rf /opt/apbs %{prefix}

%files
%defattr(-,root,root)
%{prefix}/bin
%{prefix}/lib
%{prefix}/include
#
%docdir %{prefix}/share/doc
%{prefix}/share/doc
#
%{prefix}/share/examples
%{prefix}/share/tools

%changelog
* Mon Jul 2 2012 rok
- updated for Rocks 6.0, removed pdb2pqr which is a separate roll now

* Wed Jan 26 2011 rok
- updated for APBS version 1.3 and pdb2pqr version 1.7

* Wed Jan 27 2010 rok
- updated for APBS version 1.2.1b and pdb2pqr version 1.5

* Fri Jun 6 2008 rok
- updated for 1.0.0 apbs release

* Wed Nov  9 2007 rok
- modified for 0.5.1 apbs release

* Wed Apr  4 2007 rok
- modified for 0.5.0 apbs release

* Mon Jan 30 2006 rok
- added 'Requires: coreutils' bit to fix installation problems on a
  fresh system where 'ln' might not be available yet

* Wed Jan 11 2006 rok
- fixes for 0.4.0 compilation
- added pdb2pqr sub-package

* Wed Dec 15 2004 rok
- added Todd's fix for x86_64 compilation

* Tue Dec 14 2004 rok
- added release numbering support
- added mergedx link to bin

* Fri Dec 3 2004 rok
- added PGI/Opteron support

* Tue Nov 30 2004 rok
- added Opteron support

* Sat Nov 27 2004 rok
- initial spec file

