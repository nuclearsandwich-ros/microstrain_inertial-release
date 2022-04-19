%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-microstrain-inertial-rqt
Version:        2.5.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS microstrain_inertial_rqt package

License:        BSD
URL:            https://github.com/LORD-MicroStrain/microstrain_inertial
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-microstrain-inertial-msgs
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-rclpy
Requires:       ros-humble-rqt-gui
Requires:       ros-humble-rqt-gui-py
Requires:       ros-humble-std-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-microstrain-inertial-msgs
BuildRequires:  ros-humble-nav-msgs
BuildRequires:  ros-humble-rclpy
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-rqt-gui
BuildRequires:  ros-humble-rqt-gui-py
BuildRequires:  ros-humble-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The microstrain_inertial_rqt package provides several RQT widgets to view the
status of Microstrain devices

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Apr 19 2022 Rob Fisher <rob.fisher@parker.com> - 2.5.1-2
- Autogenerated by Bloom

* Tue Feb 15 2022 Rob Fisher <rob.fisher@parker.com> - 2.5.1-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Rob Fisher <rob.fisher@parker.com> - 2.5.0-2
- Autogenerated by Bloom

