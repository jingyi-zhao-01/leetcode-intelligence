import type { Metadata } from "next";
import "./globals.css";
import { SiteHeader } from './components/site-header';

export const metadata: Metadata = {
  title: "LeetCode Pattern Tags",
  description: "Manual tagging workspace for LeetCode submissions.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>
        <SiteHeader />
        <div className="site-shell">{children}</div>
      </body>
    </html>
  );
}
