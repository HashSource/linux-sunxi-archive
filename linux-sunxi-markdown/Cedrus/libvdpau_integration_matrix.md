# Cedrus/libvdpau integration matrix
< [Cedrus][12317]
 
## Status of libvdpau-sunxi functions integration
This matrix should give us an overview of which functions are provided by [VDPAU][12320], which are required by various programs and which are already implemented in [libvdpau-sunxi][12321].  
**Notice: A '+' in the implemented field does tell us, that this feature *is* somehow integrated. It does not tell us, that it is fully completed yet or that it is free of bugs!!**
| required by [softhddevice][12322] ([VDR][12323])  | implemented (kind of) in [libvdpau-sunxi][12321]  
---|---|---  
**Bitmap Surface** |  |   
vdp_bitmap_surface_create  | \+  | \+   
vdp_bitmap_surface_destroy  | \+  | \+   
vdp_bitmap_surface_put_bits_native  | \+  | \+   
vdp_bitmap_surface_query_capabilities  | \-  | \+   
vdp_bitmap_surface_get_parameters  | \-  | \+   
|  |   
**Decoder** |  |   
vdp_decoder_create  | \+  | \+   
vdp_decoder_destroy  | \+  | \+   
vdp_decoder_query_capabilities  | \+  | \+   
vdp_decoder_render  | \+  | \+   
vdp_decoder_get_parameters  | \-  | \+   
|  |   
**Device** |  |   
vdp_device_destroy  | \+  | \+   
vdp_preemption_callback_register  | \+  | \+   
vdp_get_api_version  | \+  | \+   
vdp_get_error_string  | \+  | \+   
vdp_get_information_string  | \+  | \+   
vdp_get_proc_address  | \+  | \+   
vdp_generate_csc_matrix  | \+  | \+   
|  |   
**Output Surface** |  |   
vdp_output_surface_create  | \+  | \+   
vdp_output_surface_destroy  | \+  | \+   
vdp_output_surface_render_bitmap_surface  | \+  | \+   
vdp_output_surface_render_output_surface  | \+  | \+   
vdp_output_surface_put_bits_native  | \+  | \+   
vdp_output_surface_put_bits_indexed  | \-  | \+   
vdp_output_surface_put_bits_ycbcr  | \-  | \-   
vdp_output_surface_get_bits_native  | \+  | \-   
vdp_output_surface_get_parameters  | \+  | \+   
vdp_output_surface_query_capabilities  | \+  | \+   
vdp_output_surface_query_get_put_bits_native_capabilities  | \-  | \-   
vdp_output_surface_query_put_bits_indexed_capabilities  | \-  | \-   
vdp_output_surface_query_put_bits_ycbcr_capabilities  | \-  | \-   
|  |   
**Presentation Queue** |  |   
vdp_presentation_queue_block_until_surface_idle  | \+  | \+   
vdp_presentation_queue_create  | \+  | \+   
vdp_presentation_queue_destroy  | \+  | \+   
vdp_presentation_queue_display  | \+  | \+   
vdp_presentation_queue_set_background_color  | \+  | \+   
vdp_presentation_queue_get_background_color  | \-  | \+   
vdp_presentation_queue_get_time  | \-  | \+   
vdp_presentation_queue_target_destroy  | \+  | \+   
vdp_presentation_queue_query_surface_status  | \-  | \+   
vdp_presentation_queue_target_create_x11  | \+  | \+   
|  |   
**Video Mixer** |  |   
vdp_video_mixer_create  | \+  | \+   
vdp_video_mixer_destroy  | \+  | \+   
vdp_video_mixer_query_feature_support  | \+  | \- ([mesa][12324])   
vdp_video_mixer_query_attribute_support  | \+  | \- ([mesa][12324])   
vdp_video_mixer_query_parameter_support  | \-  | \+   
vdp_video_mixer_query_parameter_value_range  | \-  | \+   
vdp_video_mixer_query_attribute_value_range  | \-  | \+   
vdp_video_mixer_render  | \+  | \+   
vdp_video_mixer_set_attribute_values  | \+  | \+   
vdp_video_mixer_set_feature_enables  | \+  | \- ([mesa][12324])   
vdp_video_mixer_get_attribute_values  | \-  | \- ([mesa][12324])   
vdp_video_mixer_get_feature_enables  | \-  | \- ([mesa][12324])   
vdp_video_mixer_get_parameter_values  | \-  | \- ([mesa][12324])   
vdp_video_mixer_get_feature_support  | \-  | \- ([mesa][12324])   
|  |   
**Video Surface** |  |   
vdp_video_surface_create  | \+  | \+   
vdp_video_surface_destroy  | \+  | \+   
vdp_video_surface_get_bits_y_cb_cr  | \+  | \+   
vdp_video_surface_get_parameters  | \+  | \+   
vdp_video_surface_put_bits_y_cb_cr  | \+  | \+   
vdp_video_surface_query_capabilities  | \+  | \+   
vdp_video_surface_query_get_put_bits_ycbcr_capabilities  | \+  | \+
