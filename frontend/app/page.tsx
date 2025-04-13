"use client"

import { Heart, Leaf, Bot as Lotus, Users } from 'lucide-react'

import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import ChatWidget from '@/components/chatWidget'
import Image from 'next/image'
import Link from 'next/link'
import { motion } from 'framer-motion'
import { useInView } from 'react-intersection-observer'

export default function Home() {
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.1,
  })

  const fadeIn = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 }
  }

  return (
    <>
      {/* Hero Section */}
      <section className="relative h-screen flex items-center justify-center overflow-hidden">
        <Image
          src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&q=80"
          alt="Peaceful meditation scene"
          fill
          className="object-cover"
          priority
        />
        <div className="absolute inset-0 bg-black/40" />
        <div className="relative z-10 text-center text-white px-4">
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="font-serif text-5xl md:text-7xl font-bold mb-6"
          >
            Begin Your Journey Within
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="text-xl md:text-2xl mb-8 max-w-2xl mx-auto"
          >
            Transform your life through sacred ceremonies, yoga, and holistic healing in Playa del Carmen
          </motion.p>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            <Button size="lg" className="bg-accent hover:bg-accent/90 text-white">
              Explore Our Retreats
            </Button>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section ref={ref} className="py-20 px-4 bg-primary/5">
        <div className="max-w-7xl mx-auto">
          <motion.div
            variants={fadeIn}
            initial="hidden"
            animate={inView ? "visible" : "hidden"}
            transition={{ duration: 0.6 }}
            className="text-center mb-16"
          >
            <h2 className="section-heading">Your Path to Transformation</h2>
            <p className="section-subheading">
              Discover the perfect blend of ancient wisdom and modern wellness practices
            </p>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {[
              {
                icon: <Lotus className="h-8 w-8" />,
                title: "Sacred Ceremonies",
                description: "Experience profound healing through traditional mushroom ceremonies"
              },
              {
                icon: <Heart className="h-8 w-8" />,
                title: "Holistic Wellness",
                description: "Integrate mind, body, and spirit through personalized practices"
              },
              {
                icon: <Leaf className="h-8 w-8" />,
                title: "Yoga & Meditation",
                description: "Deepen your practice with expert guidance and instruction"
              },
              {
                icon: <Users className="h-8 w-8" />,
                title: "Community",
                description: "Connect with like-minded souls on the path of transformation"
              }
            ].map((feature, index) => (
              <motion.div
                key={index}
                variants={fadeIn}
                initial="hidden"
                animate={inView ? "visible" : "hidden"}
                transition={{ duration: 0.6, delay: index * 0.2 }}
              >
                <Card className="p-6 text-center hover:shadow-lg transition-shadow">
                  <div className="mb-4 text-primary flex justify-center">
                    {feature.icon}
                  </div>
                  <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                  <p className="text-muted-foreground">{feature.description}</p>
                </Card>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
      <ChatWidget />

    </>
  )
}
