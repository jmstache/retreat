import Link from 'next/link'
import { Bot as Lotus, Instagram, Facebook, Mail } from 'lucide-react'

const Footer = () => {
  return (
    <footer className="bg-primary/5 border-t">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="space-y-4">
            <Link href="/" className="flex items-center space-x-2">
              <Lotus className="h-8 w-8 text-primary" />
              <span className="font-serif text-xl font-semibold">Life Synergy</span>
            </Link>
            <p className="text-muted-foreground">
              Transformative wellness retreats in the heart of Playa del Carmen.
            </p>
            <div className="flex space-x-4">
              <a href="https://instagram.com" className="text-muted-foreground hover:text-primary">
                <Instagram className="h-5 w-5" />
              </a>
              <a href="https://facebook.com" className="text-muted-foreground hover:text-primary">
                <Facebook className="h-5 w-5" />
              </a>
              <a href="mailto:info@lifesynergyretreat.com" className="text-muted-foreground hover:text-primary">
                <Mail className="h-5 w-5" />
              </a>
            </div>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Retreats</h3>
            <ul className="space-y-2">
              <li><Link href="/retreats/wellness" className="text-muted-foreground hover:text-primary">Wellness Journey</Link></li>
              <li><Link href="/retreats/yoga" className="text-muted-foreground hover:text-primary">Yoga Immersion</Link></li>
              <li><Link href="/retreats/sacred-mushroom" className="text-muted-foreground hover:text-primary">Sacred Mushroom</Link></li>
              <li><Link href="/retreats/custom" className="text-muted-foreground hover:text-primary">Custom Retreats</Link></li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Resources</h3>
            <ul className="space-y-2">
              <li><Link href="/blog" className="text-muted-foreground hover:text-primary">Blog</Link></li>
              <li><Link href="/faq" className="text-muted-foreground hover:text-primary">FAQ</Link></li>
              <li><Link href="/preparation" className="text-muted-foreground hover:text-primary">Preparation Guide</Link></li>
              <li><Link href="/integration" className="text-muted-foreground hover:text-primary">Integration Support</Link></li>
            </ul>
          </div>

          <div>
            <h3 className="font-semibold mb-4">Contact</h3>
            <ul className="space-y-2">
              <li><Link href="/contact" className="text-muted-foreground hover:text-primary">Get in Touch</Link></li>
              <li><Link href="/location" className="text-muted-foreground hover:text-primary">Our Location</Link></li>
              <li><Link href="/book-consultation" className="text-muted-foreground hover:text-primary">Book a Consultation</Link></li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-primary/10">
          <div className="text-center text-sm text-muted-foreground">
            <p>&copy; {new Date().getFullYear()} Life Synergy Retreat. All rights reserved.</p>
            <div className="mt-2 space-x-4">
              <Link href="/privacy-policy" className="hover:text-primary">Privacy Policy</Link>
              <Link href="/terms" className="hover:text-primary">Terms of Service</Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer