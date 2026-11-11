"use client"

import { ReactNode } from 'react'
import dynamic from 'next/dynamic'

const DigitalRain = dynamic(() => import('@/components/digital-rain'), { ssr: false })

export function Providers({ children }: { children: ReactNode }) {
  return (
    <>
      <DigitalRain />
      {children}
    </>
  )
}

