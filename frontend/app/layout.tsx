import './globals.css';
import type { Metadata } from 'next';
import { Cormorant_Garamond, Poppins } from 'next/font/google';
import { ThemeProvider } from '@/components/theme-provider';
import Navigation from '@/components/navigation';
import Footer from '@/components/footer';

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