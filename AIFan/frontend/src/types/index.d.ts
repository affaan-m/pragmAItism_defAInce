/// <reference types="react" />
/// <reference types="node" />

declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}

interface Window {
  process: any;
}

declare module 'clsx' {
  type ClassValue = string | number | boolean | undefined | null | { [key: string]: any } | ClassValue[];
  
  function clsx(...inputs: ClassValue[]): string;
  export default clsx;
  export { type ClassValue };
}

declare module 'tailwind-merge' {
  export function twMerge(...inputs: string[]): string;
} 