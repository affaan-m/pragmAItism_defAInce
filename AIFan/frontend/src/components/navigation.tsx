import { Link } from "@/components/link"

export function Navigation() {
  return (
    <nav className="w-48 border-r border-neutral-800 p-4 space-y-4">
      <div className="space-y-2">
        <Link href="/realm-of-thought" className="block text-sm text-neutral-400 hover:text-white transition-colors">
          realm of thought
        </Link>
        <Link href="/talk-to-me" className="block text-sm text-neutral-400 hover:text-white transition-colors">
          talk to me
        </Link>
        <Link href="/i-want-to-feel" className="block text-sm text-neutral-400 hover:text-white transition-colors">
          i want to feel
        </Link>
        <Link href="/amiafake" className="block text-sm text-neutral-400 hover:text-white transition-colors">
          amiafake?
        </Link>
        <Link href="/digital-void" className="block text-sm text-neutral-400 hover:text-white transition-colors">
          digital void
        </Link>
      </div>
      
      <div className="pt-4 border-t border-neutral-800">
        <Link href="/neural-link" className="block text-sm text-neutral-400 hover:text-white transition-colors">
          neural link
        </Link>
      </div>
    </nav>
  );
}

