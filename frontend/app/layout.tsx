import './globals.css';

import { Cormorant_Garamond, Poppins } from 'next/font/google';

import Footer from '@/components/footer';
import type { Metadata } from 'next';
import Navigation from '@/components/navigation';
import Script from 'next/script';
import { ThemeProvider } from '@/components/theme-provider';

const serif = Cormorant_Garamond({
  subsets: ['latin'],
  variable: '--font-serif',
  display: 'swap',
  weight: ['400', '500', '600', '700'],
});

const sans = Poppins({
  subsets: ['latin'],
  variable: '--font-sans',
  display: 'swap',
  weight: ['400', '500', '600'],
});

export const metadata: Metadata = {
  title: 'Life Synergy Retreat | Wellness & Spiritual Retreats in Playa del Carmen',
  description: 'Transform your life through our holistic wellness, yoga, and sacred mushroom retreats in the heart of Playa del Carmen. Join us for a journey of healing and self-discovery.',
  keywords: 'wellness retreat, yoga retreat, spiritual retreat, mushroom ceremony, Playa del Carmen, holistic healing, meditation, mindfulness',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
      <script defer src="http://umami-go44ogggkgw4g8kowk8gso4w.138.199.163.200.sslip.io/script.js" data-website-id="bd11e9c6-9102-4e0c-ac80-d16bd5a78b53"></script>
      </head>
      <body className={`${serif.variable} ${sans.variable} font-sans antialiased`}>
        <ThemeProvider
          attribute="class"
          defaultTheme="light"
          enableSystem
          disableTransitionOnChange
        >
          <Navigation />
          <main>{children}</main>
          <Footer />
        </ThemeProvider>
      </body>
    </html>
  );
}
