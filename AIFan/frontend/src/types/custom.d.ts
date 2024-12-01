declare module 'clsx' {
  type ClassValue = string | number | boolean | undefined | null | { [key: string]: any } | ClassValue[];
  
  function clsx(...inputs: ClassValue[]): string;
  export = clsx;
}

declare module 'tailwind-merge' {
  export function twMerge(...inputs: string[]): string;
} 