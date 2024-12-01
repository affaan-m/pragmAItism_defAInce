"use client"

import { ReactNode } from 'react'

export default function ClientWrapper({ children }: { children: ReactNode }) {
  return <>{children}</>
}

