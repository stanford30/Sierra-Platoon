function AppNav(props) {
  const displayNav = () => {
    return props.navItems.map((i, index) => {
      return <a onClick={() => props.handleNavClick(i.value)}>{i.label}</a>;
    });
  };
  return <nav>{displayNav()}</nav>;
}

export default AppNav;
