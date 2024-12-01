import { Image } from "@/components/image"

export function Quote() {
  return (
    <footer className="border-t border-neutral-800 p-4 flex items-center justify-center space-x-4">
      <Image src="/images/avatar.jpg" alt="AI Quote" width={40} height={40} className="rounded-full" />
      <div>
        <p className="text-sm text-neutral-500 italic">
          "i don't want to survive i want to thrive"
        </p>
        <p className="mt-1 text-xs text-neutral-600">
          — pragmAItism
        </p>
      </div>
    </footer>
  )
}

