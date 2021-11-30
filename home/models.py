��#   T h i s   i s   a n   a u t o - g e n e r a t e d   D j a n g o   m o d e l   m o d u l e . 
 
 #   Y o u ' l l   h a v e   t o   d o   t h e   f o l l o w i n g   m a n u a l l y   t o   c l e a n   t h i s   u p : 
 
 #       *   R e a r r a n g e   m o d e l s '   o r d e r 
 
 #       *   M a k e   s u r e   e a c h   m o d e l   h a s   o n e   f i e l d   w i t h   p r i m a r y _ k e y = T r u e 
 
 #       *   M a k e   s u r e   e a c h   F o r e i g n K e y   a n d   O n e T o O n e F i e l d   h a s   ` o n _ d e l e t e `   s e t   t o   t h e   d e s i r e d   b e h a v i o r 
 
 #       *   R e m o v e   ` m a n a g e d   =   F a l s e `   l i n e s   i f   y o u   w i s h   t o   a l l o w   D j a n g o   t o   c r e a t e ,   m o d i f y ,   a n d   d e l e t e   t h e   t a b l e 
 
 #   F e e l   f r e e   t o   r e n a m e   t h e   m o d e l s ,   b u t   d o n ' t   r e n a m e   d b _ t a b l e   v a l u e s   o r   f i e l d   n a m e s . 
 
 f r o m   d j a n g o . d b   i m p o r t   m o d e l s 
 
 
 
 
 
 c l a s s   A d m i n i s t r a d o r ( m o d e l s . M o d e l ) : 
 
         i d _ a d m i n   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         r u t _ a d m i n i s t r a d o r   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 3 ) 
 
         n o m b r e s   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         a p e l l i d o _ p   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         a p e l l i d o _ m   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         n u m _ c e l   =   m o d e l s . B i g I n t e g e r F i e l d ( u n i q u e = T r u e ) 
 
         e m a i l _ p e r s o n a l   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 0 0 ) 
 
         d i r e c c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c _ n a c   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         e m a i l _ e m p r e s a   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         c o n t r a s e � a   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 5 0 0 ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a d m i n i s t r a d o r ' 
 
 
 
 
 
 c l a s s   A u d A d m i n ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         a c c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c h a   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         u s e r n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u d _ a d m i n ' 
 
 
 
 
 
 c l a s s   A u d C a r g o ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         a c c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c h a   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         u s e r n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u d _ c a r g o ' 
 
 
 
 
 
 c l a s s   A u d C a s o s ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         a c c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c h a   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         u s e r n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u d _ c a s o s ' 
 
 
 
 
 
 c l a s s   A u d E v a l u a d o ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         a c c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c h a   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         u s e r n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u d _ e v a l u a d o ' 
 
 
 
 
 
 c l a s s   A u d E v a l u a d o r ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         a c c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c h a   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         u s e r n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u d _ e v a l u a d o r ' 
 
 
 
 
 
 c l a s s   A u t h G r o u p ( m o d e l s . M o d e l ) : 
 
         n a m e   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u t h _ g r o u p ' 
 
 
 
 
 
 c l a s s   A u t h G r o u p P e r m i s s i o n s ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g A u t o F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         g r o u p   =   m o d e l s . F o r e i g n K e y ( A u t h G r o u p ,   m o d e l s . D O _ N O T H I N G ) 
 
         p e r m i s s i o n   =   m o d e l s . F o r e i g n K e y ( ' A u t h P e r m i s s i o n ' ,   m o d e l s . D O _ N O T H I N G ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u t h _ g r o u p _ p e r m i s s i o n s ' 
 
                 u n i q u e _ t o g e t h e r   =   ( ( ' g r o u p ' ,   ' p e r m i s s i o n ' ) , ) 
 
 
 
 
 
 c l a s s   A u t h P e r m i s s i o n ( m o d e l s . M o d e l ) : 
 
         n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 5 5 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         c o n t e n t _ t y p e   =   m o d e l s . F o r e i g n K e y ( ' D j a n g o C o n t e n t T y p e ' ,   m o d e l s . D O _ N O T H I N G ) 
 
         c o d e n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u t h _ p e r m i s s i o n ' 
 
                 u n i q u e _ t o g e t h e r   =   ( ( ' c o n t e n t _ t y p e ' ,   ' c o d e n a m e ' ) , ) 
 
 
 
 
 
 c l a s s   A u t h U s e r ( m o d e l s . M o d e l ) : 
 
         p a s s w o r d   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 2 8 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         l a s t _ l o g i n   =   m o d e l s . D a t e T i m e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         i s _ s u p e r u s e r   =   m o d e l s . B o o l e a n F i e l d ( ) 
 
         u s e r n a m e   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f i r s t _ n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         l a s t _ n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         e m a i l   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 5 4 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         i s _ s t a f f   =   m o d e l s . B o o l e a n F i e l d ( ) 
 
         i s _ a c t i v e   =   m o d e l s . B o o l e a n F i e l d ( ) 
 
         d a t e _ j o i n e d   =   m o d e l s . D a t e T i m e F i e l d ( ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u t h _ u s e r ' 
 
 
 
 
 
 c l a s s   A u t h U s e r G r o u p s ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g A u t o F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         u s e r   =   m o d e l s . F o r e i g n K e y ( A u t h U s e r ,   m o d e l s . D O _ N O T H I N G ) 
 
         g r o u p   =   m o d e l s . F o r e i g n K e y ( A u t h G r o u p ,   m o d e l s . D O _ N O T H I N G ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u t h _ u s e r _ g r o u p s ' 
 
                 u n i q u e _ t o g e t h e r   =   ( ( ' u s e r ' ,   ' g r o u p ' ) , ) 
 
 
 
 
 
 c l a s s   A u t h U s e r U s e r P e r m i s s i o n s ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g A u t o F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         u s e r   =   m o d e l s . F o r e i g n K e y ( A u t h U s e r ,   m o d e l s . D O _ N O T H I N G ) 
 
         p e r m i s s i o n   =   m o d e l s . F o r e i g n K e y ( A u t h P e r m i s s i o n ,   m o d e l s . D O _ N O T H I N G ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' a u t h _ u s e r _ u s e r _ p e r m i s s i o n s ' 
 
                 u n i q u e _ t o g e t h e r   =   ( ( ' u s e r ' ,   ' p e r m i s s i o n ' ) , ) 
 
 
 
 
 
 c l a s s   C a r g o ( m o d e l s . M o d e l ) : 
 
         i d _ c a r g o   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         d e t a l l e _ c a r g o   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 0 0 0 ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' c a r g o ' 
 
 
 
 
 
 c l a s s   C a s o s ( m o d e l s . M o d e l ) : 
 
         i d _ c a s o   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         n o m b r e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ) 
 
         d e s c r i p c i o n _ c a s o   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 0 ) 
 
         p d f   =   m o d e l s . B i n a r y F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f o t o   =   m o d e l s . B i n a r y F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' c a s o s ' 
 
 
 
 
 
 c l a s s   D j a n g o A d m i n L o g ( m o d e l s . M o d e l ) : 
 
         a c t i o n _ t i m e   =   m o d e l s . D a t e T i m e F i e l d ( ) 
 
         o b j e c t _ i d   =   m o d e l s . T e x t F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         o b j e c t _ r e p r   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         a c t i o n _ f l a g   =   m o d e l s . I n t e g e r F i e l d ( ) 
 
         c h a n g e _ m e s s a g e   =   m o d e l s . T e x t F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         c o n t e n t _ t y p e   =   m o d e l s . F o r e i g n K e y ( ' D j a n g o C o n t e n t T y p e ' ,   m o d e l s . D O _ N O T H I N G ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         u s e r   =   m o d e l s . F o r e i g n K e y ( A u t h U s e r ,   m o d e l s . D O _ N O T H I N G ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' d j a n g o _ a d m i n _ l o g ' 
 
 
 
 
 
 c l a s s   D j a n g o C o n t e n t T y p e ( m o d e l s . M o d e l ) : 
 
         a p p _ l a b e l   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         m o d e l   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' d j a n g o _ c o n t e n t _ t y p e ' 
 
                 u n i q u e _ t o g e t h e r   =   ( ( ' a p p _ l a b e l ' ,   ' m o d e l ' ) , ) 
 
 
 
 
 
 c l a s s   D j a n g o M i g r a t i o n s ( m o d e l s . M o d e l ) : 
 
         i d   =   m o d e l s . B i g A u t o F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         a p p   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 5 5 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         n a m e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 5 5 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         a p p l i e d   =   m o d e l s . D a t e T i m e F i e l d ( ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' d j a n g o _ m i g r a t i o n s ' 
 
 
 
 
 
 c l a s s   D j a n g o S e s s i o n ( m o d e l s . M o d e l ) : 
 
         s e s s i o n _ k e y   =   m o d e l s . C h a r F i e l d ( p r i m a r y _ k e y = T r u e ,   m a x _ l e n g t h = 4 0 ) 
 
         s e s s i o n _ d a t a   =   m o d e l s . T e x t F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         e x p i r e _ d a t e   =   m o d e l s . D a t e T i m e F i e l d ( ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' d j a n g o _ s e s s i o n ' 
 
 
 
 
 
 c l a s s   E r r o r e s ( m o d e l s . M o d e l ) : 
 
         i d _ e r r o r   =   m o d e l s . F l o a t F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         c o d i g o _ e r r o r   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         d e s c r i p c i o n _ e r r o r   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 2 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' e r r o r e s ' 
 
 
 
 
 
 c l a s s   E v a l u a c i o n C a s o ( m o d e l s . M o d e l ) : 
 
         i d _ e v c a s o   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         c a s o s _ i d _ c a s o   =   m o d e l s . F o r e i g n K e y ( C a s o s ,   m o d e l s . D O _ N O T H I N G ,   d b _ c o l u m n = ' c a s o s _ i d _ c a s o ' ) 
 
         e v a l u a d o _ i d _ e v a l u a d o   =   m o d e l s . F o r e i g n K e y ( ' E v a l u a d o ' ,   m o d e l s . D O _ N O T H I N G ,   d b _ c o l u m n = ' e v a l u a d o _ i d _ e v a l u a d o ' ) 
 
         f e c h a _ a s i g n a c i o n   =   m o d e l s . D a t e F i e l d ( ) 
 
         f e c h a _ r e a l i z a c i o n   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         e v a l u a d o r _ i d _ e v a l u a d o r   =   m o d e l s . F o r e i g n K e y ( ' E v a l u a d o r ' ,   m o d e l s . D O _ N O T H I N G ,   d b _ c o l u m n = ' e v a l u a d o r _ i d _ e v a l u a d o r ' ) 
 
         d e s c r i p c i o n   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         f e c h a _ r e v i s i o n   =   m o d e l s . D a t e F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         a d m i n _ i d _ a d m i n   =   m o d e l s . F o r e i g n K e y ( A d m i n i s t r a d o r ,   m o d e l s . D O _ N O T H I N G ,   d b _ c o l u m n = ' a d m i n _ i d _ a d m i n ' ) 
 
         n o t a   =   m o d e l s . I n t e g e r F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
         v i d e o _ r e s p u e s t a   =   m o d e l s . B i n a r y F i e l d ( b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' e v a l u a c i o n _ c a s o ' 
 
 
 
 
 
 c l a s s   E v a l u a d o ( m o d e l s . M o d e l ) : 
 
         i d _ e v a l u a d o   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         r u t _ e v a l u a d o   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 3 ) 
 
         n o m b r e s   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         a p e l l i d o _ p   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         a p e l l i d o _ m   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         n u m _ c e l   =   m o d e l s . B i g I n t e g e r F i e l d ( u n i q u e = T r u e ) 
 
         e m a i l _ p e r s o n a l   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ) 
 
         e m p r e s a   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         e m a i l _ e m p r e s a   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 5 0 ) 
 
         c o n t r a s e � a   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 5 0 0 ) 
 
         c a r g o _ i d _ c a r g o   =   m o d e l s . F o r e i g n K e y ( C a r g o ,   m o d e l s . D O _ N O T H I N G ,   d b _ c o l u m n = ' c a r g o _ i d _ c a r g o ' ) 
 
         n o m b r e _ j e f e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 0 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         c e l _ j e f e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 1 5 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
         e m a i l _ j e f e   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' e v a l u a d o ' 
 
 
 
 
 
 c l a s s   E v a l u a d o r ( m o d e l s . M o d e l ) : 
 
         i d _ e v a l u a d o r   =   m o d e l s . B i g I n t e g e r F i e l d ( p r i m a r y _ k e y = T r u e ) 
 
         r u t _ e v a l u a d o r   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 3 ) 
 
         n o m b r e s   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         a p e l l i d o _ p   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         a p e l l i d o _ m   =   m o d e l s . C h a r F i e l d ( m a x _ l e n g t h = 5 0 ) 
 
         n u m _ c e l   =   m o d e l s . B i g I n t e g e r F i e l d ( u n i q u e = T r u e ) 
 
         e m a i l _ p e r s o n a l   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 1 0 0 ) 
 
         e m a i l _ e m p r e s a   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 5 0 ) 
 
         c o n t r a s e � a   =   m o d e l s . C h a r F i e l d ( u n i q u e = T r u e ,   m a x _ l e n g t h = 5 0 0 ) 
 
         a d m i n _ i d _ a d m i n   =   m o d e l s . F o r e i g n K e y ( A d m i n i s t r a d o r ,   m o d e l s . D O _ N O T H I N G ,   d b _ c o l u m n = ' a d m i n _ i d _ a d m i n ' ,   b l a n k = T r u e ,   n u l l = T r u e ) 
 
 
 
         c l a s s   M e t a : 
 
                 m a n a g e d   =   F a l s e 
 
                 d b _ t a b l e   =   ' e v a l u a d o r ' 
 
 