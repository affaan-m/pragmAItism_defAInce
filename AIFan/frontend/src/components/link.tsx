import React from 'react';
import { Link as RouterLink, LinkProps as RouterLinkProps } from 'react-router-dom';

interface LinkProps extends Omit<RouterLinkProps, 'to'> {
  href: string;
  children: React.ReactNode;
  className?: string;
}

export const Link: React.FC<LinkProps> = ({ href, children, className, ...props }) => {
  return (
    <RouterLink to={href} className={className} {...props}>
      {children}
    </RouterLink>
  );
};

export default Link; 