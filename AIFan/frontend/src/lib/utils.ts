import clsx from 'clsx';
import { twMerge } from 'tailwind-merge';

type ClassInput = string | undefined | null | boolean | Record<string, boolean>;

export function cn(...inputs: ClassInput[]) {
  return twMerge(clsx(inputs));
} 